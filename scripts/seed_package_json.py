"""One-time: create services/<name>/package.json from pyproject versions."""

import json
from pathlib import Path

from changeset_paths import SERVICES_DIR, pkg_name, read_pyproject_version


def build_package_json(service: str, version: str) -> dict:
    return {"name": pkg_name(service), "version": version, "private": True}


def seed_dir(services_dir: Path) -> int:
    count = 0
    for svc in sorted(p for p in services_dir.iterdir() if p.is_dir()):
        pyproject = svc / "pyproject.toml"
        if not pyproject.exists():
            continue
        data = build_package_json(svc.name, read_pyproject_version(pyproject))
        (svc / "package.json").write_text(json.dumps(data, indent=2) + "\n")
        count += 1
    return count


def main() -> None:
    n = seed_dir(SERVICES_DIR)
    print(f"Seeded {n} package.json files")


if __name__ == "__main__":
    main()
