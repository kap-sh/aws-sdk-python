"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationOutputItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_attribute_display_value
    import aws_sdk_datazone.types.aggregation_attribute_value

class AggregationOutputItem(TypedDict):
    value: NotRequired["aws_sdk_datazone.types.aggregation_attribute_value.AggregationAttributeValue"]
    """<p>The attribute value of the aggregation output item.</p>"""
    count: NotRequired["int"]
    """<p>The count of the aggregation output item.</p>"""
    display_value: NotRequired["aws_sdk_datazone.types.aggregation_attribute_display_value.AggregationAttributeDisplayValue"]
    """<p>The display value of the aggregation. If the attribute being aggregated corresponds to the id of a public resource, the service automatically resolves the id to the provided display value.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AggregationOutputItem) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "count" in value:
        out["count"] = value["count"]
    if "display_value" in value:
        out["displayValue"] = value["display_value"]
    return out


def deserialize_json(data: dict) -> AggregationOutputItem:
    out: AggregationOutputItem = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "count" in data:
        out["count"] = data["count"]
    if "displayValue" in data:
        out["display_value"] = data["displayValue"]
    return out