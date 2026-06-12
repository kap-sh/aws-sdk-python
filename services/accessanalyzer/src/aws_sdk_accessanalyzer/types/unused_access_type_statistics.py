"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedAccessTypeStatistics``."""

from typing import TypedDict

from typing_extensions import NotRequired


class UnusedAccessTypeStatistics(TypedDict):
    unused_access_type: NotRequired["str"]
    """<p>The type of unused access.</p>"""
    total: NotRequired["int"]
    """<p>The total number of findings for the specified unused access type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedAccessTypeStatistics) -> dict:
    out: dict = {}
    if "unused_access_type" in value:
        out["unusedAccessType"] = value["unused_access_type"]
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> UnusedAccessTypeStatistics:
    out: UnusedAccessTypeStatistics = {}  # type: ignore[typeddict-item]
    if "unusedAccessType" in data:
        out["unused_access_type"] = data["unusedAccessType"]
    if "total" in data:
        out["total"] = data["total"]
    return out
