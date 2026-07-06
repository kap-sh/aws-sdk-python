"""Generated from Smithy shape ``com.amazonaws.inspector2#CoverageMapFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.coverage_map_comparison
    import aws_sdk_inspector2.types.non_empty_string


class CoverageMapFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.coverage_map_comparison.CoverageMapComparison"
    """<p>The operator to compare coverage on.</p>"""
    key: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag key associated with the coverage map filter.</p>"""
    value: NotRequired["aws_sdk_inspector2.types.non_empty_string.NonEmptyString"]
    """<p>The tag value associated with the coverage map filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageMapFilter) -> dict:
    out: dict = {}
    out["comparison"] = value["comparison"]
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CoverageMapFilter:
    out: CoverageMapFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        out["comparison"] = data["comparison"]
    else:
        raise DeserializationError("CoverageMapFilter.comparison required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("CoverageMapFilter.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
