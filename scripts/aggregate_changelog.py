#!/usr/bin/env python3
"""Aggregate service changelogs into root CHANGELOG.md index."""

import json
from pathlib import Path
from typing import Dict
from datetime import date


def read_manifest_changes(old_manifest: Path, new_manifest: Path) -> Dict[str, str]:
    """Detect version changes between manifest snapshots.

    Args:
        old_manifest: Path to previous manifest
        new_manifest: Path to current manifest

    Returns:
        Dict of changed packages: {"dynamodb": "0.2.0", "s3": "0.3.1"}
    """
    with open(old_manifest) as f:
        old_data = json.load(f)

    with open(new_manifest) as f:
        new_data = json.load(f)

    changes = {}
    for path, new_version in new_data.items():
        old_version = old_data.get(path)
        if old_version != new_version:
            # Extract service name from path
            service_name = path.split("/")[-1]
            changes[service_name] = new_version

    return changes


def generate_root_changelog(
    changed_packages: Dict[str, str],
    changelog_path: Path,
    release_date: str
) -> None:
    """Generate or update root CHANGELOG.md with release index.

    Args:
        changed_packages: Dict of service names to new versions
        changelog_path: Path to root CHANGELOG.md
        release_date: ISO date string for release section
    """
    # Read existing changelog or create header
    header = "# AWS SDK for Python - Releases\n\n"
    if changelog_path.exists():
        existing_content = changelog_path.read_text()
        # Strip header to re-add it
        if existing_content.startswith(header):
            existing_content = existing_content[len(header):]
    else:
        existing_content = ""

    # Build new release section
    new_section = f"## {release_date}\n\n"

    for service_name in sorted(changed_packages.keys()):
        version = changed_packages[service_name]
        link = f"services/{service_name}/CHANGELOG.md"
        new_section += f"- [aws-sdk-{service_name} v{version}]({link})\n"

    new_section += "\n"

    # Combine: header + new section + existing
    final_content = header + new_section + existing_content

    changelog_path.write_text(final_content)


def main() -> None:
    """Main entry point - aggregate changelogs after release-please runs."""
    import subprocess

    repo_root = Path(__file__).parent.parent
    manifest_path = repo_root / ".release-please-manifest.json"
    changelog_path = repo_root / "CHANGELOG.md"

    # Get manifest from previous commit
    result = subprocess.run(
        ["git", "show", "HEAD~1:.release-please-manifest.json"],
        capture_output=True,
        text=True,
        cwd=repo_root
    )

    if result.returncode != 0:
        print("No previous manifest found - creating initial changelog")
        # First run - include all packages
        with open(manifest_path) as f:
            all_packages = json.load(f)

        changed_packages = {
            path.split("/")[-1]: version
            for path, version in all_packages.items()
        }
    else:
        # Compare manifests
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write(result.stdout)
            old_manifest_path = Path(f.name)

        changed_packages = read_manifest_changes(old_manifest_path, manifest_path)
        old_manifest_path.unlink()

    if not changed_packages:
        print("No package version changes detected")
        return

    print(f"Aggregating changelog for {len(changed_packages)} changed packages...")

    today = date.today().isoformat()
    generate_root_changelog(changed_packages, changelog_path, today)

    print(f"✓ Root changelog updated: {changelog_path}")


if __name__ == "__main__":
    main()
