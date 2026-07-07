"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterAggMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agg_type
    import aws_sdk_quicksight.types.identifier
    import aws_sdk_quicksight.types.topic_sort_direction


class FilterAggMetrics(TypedDict, closed=True):
    metric_operand: NotRequired["aws_sdk_quicksight.types.identifier.Identifier"]
    """<p>The metric operand of the <code>FilterAggMetrics</code>.</p>"""
    function: NotRequired["aws_sdk_quicksight.types.agg_type.AggType"]
    """<p>The function for the <code>FilterAggMetrics</code>.</p>"""
    sort_direction: NotRequired[
        "aws_sdk_quicksight.types.topic_sort_direction.TopicSortDirection"
    ]
    """<p>The sort direction for <code>FilterAggMetrics</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAggMetrics) -> dict:
    out: dict = {}
    if "metric_operand" in value:
        import aws_sdk_quicksight.types.identifier

        out["MetricOperand"] = aws_sdk_quicksight.types.identifier.serialize_json(
            value["metric_operand"]
        )
    if "function" in value:
        import aws_sdk_quicksight.types.agg_type

        out["Function"] = aws_sdk_quicksight.types.agg_type.serialize_json(
            value["function"]
        )
    if "sort_direction" in value:
        import aws_sdk_quicksight.types.topic_sort_direction

        out["SortDirection"] = (
            aws_sdk_quicksight.types.topic_sort_direction.serialize_json(
                value["sort_direction"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterAggMetrics:
    out: FilterAggMetrics = {}  # type: ignore[typeddict-item]
    if "MetricOperand" in data:
        import aws_sdk_quicksight.types.identifier

        out["metric_operand"] = aws_sdk_quicksight.types.identifier.deserialize_json(
            data["MetricOperand"]
        )
    if "Function" in data:
        import aws_sdk_quicksight.types.agg_type

        out["function"] = aws_sdk_quicksight.types.agg_type.deserialize_json(
            data["Function"]
        )
    if "SortDirection" in data:
        import aws_sdk_quicksight.types.topic_sort_direction

        out["sort_direction"] = (
            aws_sdk_quicksight.types.topic_sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    return out
