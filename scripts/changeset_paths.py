"""Shared helpers for changeset generation and version sync."""

import re
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
SERVICES_DIR = REPO_ROOT / "services"

# A staged path bumps its service only if it matches one of these (relative to
# the service dir). Everything else (README.md, CHANGELOG.md, tests/**, *.md) is
# treated as non-releasable.
_BUMP_INCLUDE_PREFIXES = ("src/",)
_BUMP_INCLUDE_FILES = ("pyproject.toml",)

_VERSION_RE = re.compile(r'^version\s*=\s*"([^"]+)"', re.MULTILINE)


def path_to_service(path: str) -> Optional[str]:
    """Return service name for a repo-relative path, or None if not in services/."""
    parts = Path(path).parts
    if len(parts) >= 2 and parts[0] == "services":
        return parts[1]
    return None


def path_bumps_service(path: str) -> bool:
    """True if this path should trigger a version bump for its service."""
    parts = Path(path).parts
    if len(parts) < 3 or parts[0] != "services":
        return False
    rel = "/".join(parts[2:])
    if rel in _BUMP_INCLUDE_FILES:
        return True
    return any(rel.startswith(p) for p in _BUMP_INCLUDE_PREFIXES)


def read_pyproject_version(pyproject: Path) -> str:
    """Return the top-level project version string from a pyproject.toml."""
    m = _VERSION_RE.search(pyproject.read_text())
    if not m:
        raise ValueError(f"no version in {pyproject}")
    return m.group(1)


def write_pyproject_version(pyproject: Path, version: str) -> None:
    """Replace the top-level project version in a pyproject.toml in place."""
    text = pyproject.read_text()
    new, n = _VERSION_RE.subn(f'version = "{version}"', text, count=1)
    if n != 1:
        raise ValueError(f"no version to replace in {pyproject}")
    pyproject.write_text(new)


def pkg_name(service: str) -> str:
    return f"aws-sdk-{service}"
