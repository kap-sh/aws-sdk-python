"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.aggregation_display_value
    import capo_datazone.types.aggregation_output_items
    import capo_datazone.types.attribute


class AggregationOutput(TypedDict, closed=True):
    attribute: NotRequired["capo_datazone.types.attribute.Attribute"]
    """<p>The attribute for this aggregation.</p>"""
    display_value: NotRequired[
        "capo_datazone.types.aggregation_display_value.AggregationDisplayValue"
    ]
    """<p>The display value of the aggregation output item.</p>"""
    items: NotRequired[
        "capo_datazone.types.aggregation_output_items.AggregationOutputItems"
    ]
    """<p>A list of aggregation output items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationOutput) -> dict:
    out: dict = {}
    if "attribute" in value:
        out["attribute"] = value["attribute"]
    if "display_value" in value:
        out["displayValue"] = value["display_value"]
    if "items" in value:
        import capo_datazone.types.aggregation_output_items

        out["items"] = capo_datazone.types.aggregation_output_items.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> AggregationOutput:
    out: AggregationOutput = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        out["attribute"] = data["attribute"]
    if "displayValue" in data:
        out["display_value"] = data["displayValue"]
    if "items" in data:
        import capo_datazone.types.aggregation_output_items

        out["items"] = capo_datazone.types.aggregation_output_items.deserialize_json(
            data["items"]
        )
    return out
