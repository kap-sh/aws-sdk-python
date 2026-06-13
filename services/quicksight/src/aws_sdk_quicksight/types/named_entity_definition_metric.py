"""Generated from Smithy shape ``com.amazonaws.quicksight#NamedEntityDefinitionMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function_parameters
    import aws_sdk_quicksight.types.named_entity_agg_type


class NamedEntityDefinitionMetric(TypedDict):
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.named_entity_agg_type.NamedEntityAggType"
    ]
    """<p>The aggregation of a named entity. Valid values for this structure are <code>SUM</code>, <code>MIN</code>, <code>MAX</code>, <code>COUNT</code>, <code>AVERAGE</code>, <code>DISTINCT_COUNT</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, <code>VARP</code>, <code>PERCENTILE</code>, <code>MEDIAN</code>, and <code>CUSTOM</code>.</p>"""
    aggregation_function_parameters: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function_parameters.AggregationFunctionParameters"
    ]
    """<p>The additional parameters for an aggregation function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NamedEntityDefinitionMetric) -> dict:
    out: dict = {}
    if "aggregation" in value:
        import aws_sdk_quicksight.types.named_entity_agg_type

        out["Aggregation"] = (
            aws_sdk_quicksight.types.named_entity_agg_type.serialize_json(
                value["aggregation"]
            )
        )
    if "aggregation_function_parameters" in value:
        import aws_sdk_quicksight.types.aggregation_function_parameters

        out["AggregationFunctionParameters"] = (
            aws_sdk_quicksight.types.aggregation_function_parameters.serialize_json(
                value["aggregation_function_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> NamedEntityDefinitionMetric:
    out: NamedEntityDefinitionMetric = {}  # type: ignore[typeddict-item]
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.named_entity_agg_type

        out["aggregation"] = (
            aws_sdk_quicksight.types.named_entity_agg_type.deserialize_json(
                data["Aggregation"]
            )
        )
    if "AggregationFunctionParameters" in data:
        import aws_sdk_quicksight.types.aggregation_function_parameters

        out["aggregation_function_parameters"] = (
            aws_sdk_quicksight.types.aggregation_function_parameters.deserialize_json(
                data["AggregationFunctionParameters"]
            )
        )
    return out
