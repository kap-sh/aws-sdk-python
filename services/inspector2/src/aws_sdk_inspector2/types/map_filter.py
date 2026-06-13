"""Generated from Smithy shape ``com.amazonaws.inspector2#MapFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.map_comparison
    import aws_sdk_inspector2.types.map_key
    import aws_sdk_inspector2.types.map_value


class MapFilter(TypedDict):
    comparison: "aws_sdk_inspector2.types.map_comparison.MapComparison"
    """<p>The operator to use when comparing values in the filter.</p>"""
    key: "aws_sdk_inspector2.types.map_key.MapKey"
    """<p>The tag key used in the filter.</p>"""
    value: NotRequired["aws_sdk_inspector2.types.map_value.MapValue"]
    """<p>The tag value used in the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MapFilter:
    out: MapFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        out["comparison"] = data["comparison"]
    else:
        raise DeserializationError("MapFilter.comparison required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("MapFilter.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
