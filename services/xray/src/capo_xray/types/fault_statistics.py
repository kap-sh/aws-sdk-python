"""Generated from Smithy shape ``com.amazonaws.xray#FaultStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.nullable_long


class FaultStatistics(TypedDict, closed=True):
    other_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The number of requests that failed with untracked 5xx Server Error status codes.</p>"""
    total_count: NotRequired["capo_xray.types.nullable_long.NullableLong"]
    """<p>The total number of requests that failed with a 5xx Server Error status code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FaultStatistics) -> dict:
    out: dict = {}
    if "other_count" in value:
        out["OtherCount"] = value["other_count"]
    if "total_count" in value:
        out["TotalCount"] = value["total_count"]
    return out


def deserialize_json(data: dict) -> FaultStatistics:
    out: FaultStatistics = {}  # type: ignore[typeddict-item]
    if "OtherCount" in data:
        out["other_count"] = data["OtherCount"]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    return out
