"""Generated from Smithy shape ``com.amazonaws.inspector2#StatusCounts``."""

from typing_extensions import NotRequired, TypedDict


class StatusCounts(TypedDict, closed=True):
    failed: NotRequired["int"]
    """<p>The number of checks that failed.</p>"""
    skipped: NotRequired["int"]
    """<p>The number of checks that were skipped.</p>"""
    passed: NotRequired["int"]
    """<p>The number of checks that passed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusCounts) -> dict:
    out: dict = {}
    if "failed" in value:
        out["failed"] = value["failed"]
    if "skipped" in value:
        out["skipped"] = value["skipped"]
    if "passed" in value:
        out["passed"] = value["passed"]
    return out


def deserialize_json(data: dict) -> StatusCounts:
    out: StatusCounts = {}  # type: ignore[typeddict-item]
    if "failed" in data:
        out["failed"] = data["failed"]
    if "skipped" in data:
        out["skipped"] = data["skipped"]
    if "passed" in data:
        out["passed"] = data["passed"]
    return out
