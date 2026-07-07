"""Generated from Smithy shape ``com.amazonaws.pinpoint#MetricDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__double
    import aws_sdk_pinpoint.types.__string


class MetricDimension(TypedDict, closed=True):
    comparison_operator: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The operator to use when comparing metric values. Valid values are: GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUAL, LESS_THAN_OR_EQUAL, and EQUAL.</p>"""
    value: NotRequired["aws_sdk_pinpoint.types.__double.__double"]
    """<p>The value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDimension) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        out["ComparisonOperator"] = value["comparison_operator"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    if "ComparisonOperator" in data:
        out["comparison_operator"] = data["ComparisonOperator"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
