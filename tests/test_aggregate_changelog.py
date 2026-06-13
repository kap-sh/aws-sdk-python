# tests/test_aggregate_changelog.py
import json
import tempfile
from pathlib import Path
from datetime import date
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from aggregate_changelog import read_manifest_changes, generate_root_changelog


def test_read_manifest_changes():
    """Test detecting version changes between commits"""
    with tempfile.TemporaryDirectory() as tmpdir:
        manifest_old = Path(tmpdir) / "manifest_old.json"
        manifest_new = Path(tmpdir) / "manifest_new.json"

        manifest_old.write_text(json.dumps({
            "services/dynamodb": "0.1.0",
            "services/s3": "0.2.0",
            "services/iam": "0.1.0"
        }))

        manifest_new.write_text(json.dumps({
            "services/dynamodb": "0.2.0",  # Changed
            "services/s3": "0.2.0",        # Unchanged
            "services/iam": "0.1.1"        # Changed
        }))

        changes = read_manifest_changes(manifest_old, manifest_new)

        assert changes == {
            "dynamodb": "0.2.0",
            "iam": "0.1.1"
        }


def test_generate_root_changelog():
    """Test root changelog generation"""
    changed_packages = {
        "dynamodb": "0.2.0",
        "s3": "0.3.1",
        "lambda": "0.4.0"
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        changelog_path = Path(tmpdir) / "CHANGELOG.md"
        existing_content = """# AWS SDK for Python - Releases

## 2024-06-10

- [aws-sdk-iam v0.1.2](services/iam/CHANGELOG.md)
"""
        changelog_path.write_text(existing_content)

        today = date.today().isoformat()
        generate_root_changelog(changed_packages, changelog_path, today)

        content = changelog_path.read_text()

        # Check new entry added at top
        assert f"## {today}" in content
        assert "[aws-sdk-dynamodb v0.2.0](services/dynamodb/CHANGELOG.md)" in content
        assert "[aws-sdk-s3 v0.3.1](services/s3/CHANGELOG.md)" in content
        assert "[aws-sdk-lambda v0.4.0](services/lambda/CHANGELOG.md)" in content

        # Check existing content preserved
        assert "## 2024-06-10" in content
        assert "[aws-sdk-iam v0.1.2](services/iam/CHANGELOG.md)" in content
