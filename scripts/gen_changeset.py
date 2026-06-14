"""Generate a changeset file from staged git changes.

Usage: python scripts/gen_changeset.py [--bump minor|patch|major|none] [--summary TEXT]
"""

import argparse
import subprocess
import uuid
from typing import Iterable, Set

from changeset_paths import REPO_ROOT, path_bumps_service, path_to_service, pkg_name

CHANGESET_DIR = REPO_ROOT / ".changeset"


def staged_paths() -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--staged", "--name-only"],
        capture_output=True, text=True, check=True, cwd=REPO_ROOT,
    ).stdout
    return [line for line in out.splitlines() if line.strip()]


def affected_services(paths: Iterable[str]) -> Set[str]:
    services = set()
    for p in paths:
        if path_bumps_service(p):
            svc = path_to_service(p)
            if svc is not None:
                services.add(svc)
    return services


def render_changeset(services: Set[str], bump: str, summary: str) -> str:
    lines = ["---"]
    if services and bump != "none":
        for svc in sorted(services):
            lines.append(f'"{pkg_name(svc)}": {bump}')
    lines.append("---")
    lines.append("")
    lines.append(summary)
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bump", choices=["minor", "patch", "major", "none"], default="minor")
    parser.add_argument("--summary", default="Update service")
    args = parser.parse_args()

    services = affected_services(staged_paths())
    if args.bump != "none" and not services:
        print("No releasable service changes staged; emitting empty changeset")

    # render_changeset emits empty frontmatter when bump == "none" or no services.
    emitted = services if args.bump != "none" else set()
    content = render_changeset(services, args.bump, args.summary)
    CHANGESET_DIR.mkdir(exist_ok=True)
    out = CHANGESET_DIR / f"{uuid.uuid4().hex[:8]}.md"
    out.write_text(content)
    print(f"Wrote {out} ({len(emitted)} services, bump={args.bump})")


if __name__ == "__main__":
    main()
