"""Generated from Smithy shape ``com.amazonaws.quicksight#AggFunction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agg_function_param_map
    import aws_sdk_quicksight.types.agg_type
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.topic_time_granularity


class AggFunction(TypedDict):
    aggregation: NotRequired["aws_sdk_quicksight.types.agg_type.AggType"]
    """<p>The aggregation of an Agg function.</p>"""
    aggregation_function_parameters: NotRequired[
        "aws_sdk_quicksight.types.agg_function_param_map.AggFunctionParamMap"
    ]
    """<p>The aggregation parameters for an Agg function.</p>"""
    period: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The period of an Agg function.</p>"""
    period_field: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The period field for an Agg function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggFunction) -> dict:
    out: dict = {}
    if "aggregation" in value:
        import aws_sdk_quicksight.types.agg_type

        out["Aggregation"] = aws_sdk_quicksight.types.agg_type.serialize_json(
            value["aggregation"]
        )
    if "aggregation_function_parameters" in value:
        import aws_sdk_quicksight.types.agg_function_param_map

        out["AggregationFunctionParameters"] = (
            aws_sdk_quicksight.types.agg_function_param_map.serialize_json(
                value["aggregation_function_parameters"]
            )
        )
    if "period" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["Period"] = aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
            value["period"]
        )
    if "period_field" in value:
        out["PeriodField"] = value["period_field"]
    return out


def deserialize_json(data: dict) -> AggFunction:
    out: AggFunction = {}  # type: ignore[typeddict-item]
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.agg_type

        out["aggregation"] = aws_sdk_quicksight.types.agg_type.deserialize_json(
            data["Aggregation"]
        )
    if "AggregationFunctionParameters" in data:
        import aws_sdk_quicksight.types.agg_function_param_map

        out["aggregation_function_parameters"] = (
            aws_sdk_quicksight.types.agg_function_param_map.deserialize_json(
                data["AggregationFunctionParameters"]
            )
        )
    if "Period" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["period"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["Period"]
            )
        )
    if "PeriodField" in data:
        out["period_field"] = data["PeriodField"]
    return out
