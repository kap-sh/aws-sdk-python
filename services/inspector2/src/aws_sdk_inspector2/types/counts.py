"""Generated from Smithy shape ``com.amazonaws.inspector2#Counts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.agg_counts
    import aws_sdk_inspector2.types.group_key


class Counts(TypedDict):
    count: "aws_sdk_inspector2.types.agg_counts.AggCounts"
    """<p>The number of resources.</p>"""
    group_key: NotRequired["aws_sdk_inspector2.types.group_key.GroupKey"]
    """<p>The key associated with this group</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Counts) -> dict:
    out: dict = {}
    out["count"] = value.get("count", 0)
    if "group_key" in value:
        out["groupKey"] = value["group_key"]
    return out


def deserialize_json(data: dict) -> Counts:
    out: Counts = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if "groupKey" in data:
        out["group_key"] = data["groupKey"]
    return out
