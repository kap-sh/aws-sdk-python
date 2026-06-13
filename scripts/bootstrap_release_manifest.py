#!/usr/bin/env python3
"""Bootstrap release-please manifest by scanning service package versions."""

import json
import tomllib
from pathlib import Path
from typing import Dict


def scan_services(services_dir: Path) -> Dict[str, str]:
    """Scan all service directories for package versions.

    Args:
        services_dir: Path to services directory containing package folders

    Returns:
        Dict mapping service paths to versions, e.g.:
        {"services/dynamodb": "0.1.0", "services/s3": "0.2.5"}
    """
    package_versions = {}

    for service_dir in sorted(services_dir.iterdir()):
        if not service_dir.is_dir():
            continue

        pyproject_path = service_dir / "pyproject.toml"
        if not pyproject_path.exists():
            continue

        with open(pyproject_path, "rb") as f:
            data = tomllib.load(f)

        version = data.get("project", {}).get("version")
        if version:
            # Use relative path from repo root
            rel_path = f"services/{service_dir.name}"
            package_versions[rel_path] = version

    return package_versions


def generate_manifest(package_versions: Dict[str, str], output_path: Path) -> None:
    """Write package versions to release-please manifest JSON.

    Args:
        package_versions: Dict of service paths to versions
        output_path: Path to write .release-please-manifest.json
    """
    with open(output_path, "w") as f:
        json.dump(package_versions, f, indent=2, sort_keys=True)
        f.write("\n")  # Trailing newline


def main() -> None:
    """Main entry point - scan services and generate manifest."""
    repo_root = Path(__file__).parent.parent
    services_dir = repo_root / "services"
    manifest_path = repo_root / ".release-please-manifest.json"

    print(f"Scanning services in {services_dir}...")
    package_versions = scan_services(services_dir)

    print(f"Found {len(package_versions)} packages")

    print(f"Writing manifest to {manifest_path}...")
    generate_manifest(package_versions, manifest_path)

    print("✓ Manifest generated successfully")


if __name__ == "__main__":
    main()
