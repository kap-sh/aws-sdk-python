# tests/test_bootstrap_manifest.py
import json
import tempfile
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from bootstrap_release_manifest import scan_services, generate_manifest


def test_scan_services_extracts_versions():
    """Test scanning pyproject.toml files for versions"""
    with tempfile.TemporaryDirectory() as tmpdir:
        services_dir = Path(tmpdir) / "services"

        # Create test service structure
        svc1 = services_dir / "dynamodb"
        svc1.mkdir(parents=True)
        (svc1 / "pyproject.toml").write_text(
            '[project]\nname = "aws-sdk-dynamodb"\nversion = "0.1.0"\n'
        )

        svc2 = services_dir / "s3"
        svc2.mkdir(parents=True)
        (svc2 / "pyproject.toml").write_text(
            '[project]\nname = "aws-sdk-s3"\nversion = "0.2.5"\n'
        )

        result = scan_services(services_dir)

        assert result == {
            "services/dynamodb": "0.1.0",
            "services/s3": "0.2.5"
        }


def test_generate_manifest_creates_json():
    """Test manifest JSON generation"""
    package_versions = {
        "services/iam": "0.1.0",
        "services/kms": "0.3.2"
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        manifest_path = Path(tmpdir) / ".release-please-manifest.json"
        generate_manifest(package_versions, manifest_path)

        with open(manifest_path) as f:
            data = json.load(f)

        assert data == package_versions
