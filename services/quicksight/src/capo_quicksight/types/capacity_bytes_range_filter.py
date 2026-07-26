"""Generated from Smithy shape ``com.amazonaws.quicksight#CapacityBytesRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.capacity_bytes_range_filter_max_bytes_long
    import capo_quicksight.types.capacity_bytes_range_filter_min_bytes_long


class CapacityBytesRangeFilter(TypedDict, closed=True):
    min_bytes: NotRequired[
        "capo_quicksight.types.capacity_bytes_range_filter_min_bytes_long.CapacityBytesRangeFilterMinBytesLong"
    ]
    """<p>The minimum capacity in bytes (inclusive). At least one of minBytes or maxBytes is required.</p>"""
    max_bytes: NotRequired[
        "capo_quicksight.types.capacity_bytes_range_filter_max_bytes_long.CapacityBytesRangeFilterMaxBytesLong"
    ]
    """<p>The maximum capacity in bytes (inclusive). At least one of minBytes or maxBytes is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityBytesRangeFilter) -> dict:
    out: dict = {}
    if "min_bytes" in value:
        out["minBytes"] = value["min_bytes"]
    if "max_bytes" in value:
        out["maxBytes"] = value["max_bytes"]
    return out


def deserialize_json(data: dict) -> CapacityBytesRangeFilter:
    out: CapacityBytesRangeFilter = {}  # type: ignore[typeddict-item]
    if "minBytes" in data:
        out["min_bytes"] = data["minBytes"]
    if "maxBytes" in data:
        out["max_bytes"] = data["maxBytes"]
    return out
