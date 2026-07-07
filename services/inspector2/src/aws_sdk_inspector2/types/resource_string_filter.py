"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceStringFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.resource_string_comparison
    import aws_sdk_inspector2.types.resource_string_input


class ResourceStringFilter(TypedDict, closed=True):
    comparison: (
        "aws_sdk_inspector2.types.resource_string_comparison.ResourceStringComparison"
    )
    """<p>The filter's comparison.</p>"""
    value: "aws_sdk_inspector2.types.resource_string_input.ResourceStringInput"
    """<p>The filter's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStringFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ResourceStringFilter:
    out: ResourceStringFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        out["comparison"] = data["comparison"]
    else:
        raise DeserializationError("ResourceStringFilter.comparison required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("ResourceStringFilter.value required")
    return out
