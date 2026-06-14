"""Copy each service's package.json version into its pyproject.toml.

Run after `changeset version`.
"""

import json
from pathlib import Path

from changeset_paths import SERVICES_DIR, read_pyproject_version, write_pyproject_version


def sync_dir(services_dir: Path) -> list[str]:
    changed = []
    for svc in sorted(p for p in services_dir.iterdir() if p.is_dir()):
        pkg = svc / "package.json"
        pyproject = svc / "pyproject.toml"
        if not pkg.exists() or not pyproject.exists():
            continue
        target = json.loads(pkg.read_text())["version"]
        if read_pyproject_version(pyproject) != target:
            write_pyproject_version(pyproject, target)
            changed.append(svc.name)
    return changed


def main() -> None:
    changed = sync_dir(SERVICES_DIR)
    print(f"Synced {len(changed)} pyproject.toml versions: {', '.join(changed) or '(none)'}")


if __name__ == "__main__":
    main()
