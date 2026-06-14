#!/usr/bin/env python3
"""Aggregate service changelogs into root CHANGELOG.md index.

Derives changed services from the pyproject.toml version diff between the working
tree and HEAD (post `changeset version` + sync_pyproject, before the changesets
action commits).
"""

import subprocess
from datetime import date
from pathlib import Path
from typing import Dict, Optional

from changeset_paths import REPO_ROOT, _VERSION_RE, pkg_name


def _extract(text: str) -> Optional[str]:
    m = _VERSION_RE.search(text)
    return m.group(1) if m else None


def changed_services(repo_root: Path) -> Dict[str, str]:
    """Return {service: new_version} for services whose pyproject version changed
    in the working tree relative to HEAD.

    Run inside the changesets `version` step, where `changeset version` and
    sync_pyproject have edited pyproject.toml in the working tree but not yet
    committed. The new version is read from the working-tree file; the old
    version from HEAD.
    """
    changed_paths = subprocess.run(
        ["git", "diff", "HEAD", "--name-only", "--", "services/*/pyproject.toml"],
        capture_output=True, text=True, cwd=repo_root,
    ).stdout.splitlines()

    result: Dict[str, str] = {}
    for path in changed_paths:
        parts = Path(path).parts
        if len(parts) < 2:
            continue
        service = parts[1]
        new_ver = _extract((repo_root / path).read_text())
        old = subprocess.run(
            ["git", "show", f"HEAD:{path}"],
            capture_output=True, text=True, cwd=repo_root,
        )
        old_ver = _extract(old.stdout) if old.returncode == 0 else None
        if new_ver and new_ver != old_ver:
            result[service] = new_ver
    return result


def generate_root_changelog(
    changed_packages: Dict[str, str],
    changelog_path: Path,
    release_date: str,
) -> None:
    header = "# AWS SDK for Python - Releases\n\n"
    existing = ""
    if changelog_path.exists():
        existing = changelog_path.read_text()
        if existing.startswith(header):
            existing = existing[len(header):]

    section = f"## {release_date}\n\n"
    for service in sorted(changed_packages):
        version = changed_packages[service]
        section += f"- [{pkg_name(service)} v{version}](services/{service}/CHANGELOG.md)\n"
    section += "\n"

    changelog_path.write_text(header + section + existing)


def main() -> None:
    changed = changed_services(REPO_ROOT)
    if not changed:
        print("No package version changes detected")
        return
    print(f"Aggregating changelog for {len(changed)} changed packages...")
    generate_root_changelog(changed, REPO_ROOT / "CHANGELOG.md", date.today().isoformat())
    print("✓ Root changelog updated")


if __name__ == "__main__":
    main()
