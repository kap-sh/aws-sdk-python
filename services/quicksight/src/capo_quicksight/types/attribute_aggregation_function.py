"""Generated from Smithy shape ``com.amazonaws.quicksight#AttributeAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.simple_attribute_aggregation_function
    import capo_quicksight.types.string


class AttributeAggregationFunction(TypedDict, closed=True):
    simple_attribute_aggregation: NotRequired[
        "capo_quicksight.types.simple_attribute_aggregation_function.SimpleAttributeAggregationFunction"
    ]
    """<p>The built-in aggregation functions for attributes.</p> <ul> <li> <p> <code>UNIQUE_VALUE</code>: Returns the unique value for a field, aggregated by the dimension fields.</p> </li> </ul>"""
    value_for_multiple_values: NotRequired["capo_quicksight.types.string.String"]
    """<p>Used by the <code>UNIQUE_VALUE</code> aggregation function. If there are multiple values for the field used by the aggregation, the value for this property will be returned instead. Defaults to '*'.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeAggregationFunction) -> dict:
    out: dict = {}
    if "simple_attribute_aggregation" in value:
        import capo_quicksight.types.simple_attribute_aggregation_function

        out["SimpleAttributeAggregation"] = (
            capo_quicksight.types.simple_attribute_aggregation_function.serialize_json(
                value["simple_attribute_aggregation"]
            )
        )
    if "value_for_multiple_values" in value:
        out["ValueForMultipleValues"] = value["value_for_multiple_values"]
    return out


def deserialize_json(data: dict) -> AttributeAggregationFunction:
    out: AttributeAggregationFunction = {}  # type: ignore[typeddict-item]
    if "SimpleAttributeAggregation" in data:
        import capo_quicksight.types.simple_attribute_aggregation_function

        out["simple_attribute_aggregation"] = (
            capo_quicksight.types.simple_attribute_aggregation_function.deserialize_json(
                data["SimpleAttributeAggregation"]
            )
        )
    if "ValueForMultipleValues" in data:
        out["value_for_multiple_values"] = data["ValueForMultipleValues"]
    return out
