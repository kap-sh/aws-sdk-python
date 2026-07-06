"""Generated from Smithy shape ``com.amazonaws.inspector2#SeverityCounts``."""

from typing_extensions import NotRequired, TypedDict


class SeverityCounts(TypedDict, closed=True):
    all: NotRequired["int"]
    """<p>The total count of findings from all severities.</p>"""
    medium: NotRequired["int"]
    """<p>The total count of medium severity findings.</p>"""
    high: NotRequired["int"]
    """<p>The total count of high severity findings.</p>"""
    critical: NotRequired["int"]
    """<p>The total count of critical severity findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeverityCounts) -> dict:
    out: dict = {}
    if "all" in value:
        out["all"] = value["all"]
    if "medium" in value:
        out["medium"] = value["medium"]
    if "high" in value:
        out["high"] = value["high"]
    if "critical" in value:
        out["critical"] = value["critical"]
    return out


def deserialize_json(data: dict) -> SeverityCounts:
    out: SeverityCounts = {}  # type: ignore[typeddict-item]
    if "all" in data:
        out["all"] = data["all"]
    if "medium" in data:
        out["medium"] = data["medium"]
    if "high" in data:
        out["high"] = data["high"]
    if "critical" in data:
        out["critical"] = data["critical"]
    return out
