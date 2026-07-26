"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.resource_map_comparison


class ResourceMapFilter(TypedDict, closed=True):
    comparison: "capo_inspector2.types.resource_map_comparison.ResourceMapComparison"
    """<p>The filter's comparison.</p>"""
    key: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The filter's key.</p>"""
    value: NotRequired["capo_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The filter's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ResourceMapFilter:
    out: ResourceMapFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        out["comparison"] = data["comparison"]
    else:
        raise DeserializationError("ResourceMapFilter.comparison required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ResourceMapFilter.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
