"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationListItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_display_value
    import aws_sdk_datazone.types.attribute


class AggregationListItem(TypedDict):
    attribute: "aws_sdk_datazone.types.attribute.Attribute"
    """<p>An attribute on which to compute aggregations.</p>"""
    display_value: NotRequired[
        "aws_sdk_datazone.types.aggregation_display_value.AggregationDisplayValue"
    ]
    """<p>The display value of the aggregation list item. Supported values include <code>value</code> and <code>glossaryTerm.name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationListItem) -> dict:
    out: dict = {}
    out["attribute"] = value["attribute"]
    if "display_value" in value:
        out["displayValue"] = value["display_value"]
    return out


def deserialize_json(data: dict) -> AggregationListItem:
    out: AggregationListItem = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        out["attribute"] = data["attribute"]
    else:
        raise DeserializationError("AggregationListItem.attribute required")
    if "displayValue" in data:
        out["display_value"] = data["displayValue"]
    return out
