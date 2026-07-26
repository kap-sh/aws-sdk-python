"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterAggMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agg_type
    import capo_quicksight.types.identifier
    import capo_quicksight.types.topic_sort_direction


class FilterAggMetrics(TypedDict, closed=True):
    metric_operand: NotRequired["capo_quicksight.types.identifier.Identifier"]
    """<p>The metric operand of the <code>FilterAggMetrics</code>.</p>"""
    function: NotRequired["capo_quicksight.types.agg_type.AggType"]
    """<p>The function for the <code>FilterAggMetrics</code>.</p>"""
    sort_direction: NotRequired[
        "capo_quicksight.types.topic_sort_direction.TopicSortDirection"
    ]
    """<p>The sort direction for <code>FilterAggMetrics</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterAggMetrics) -> dict:
    out: dict = {}
    if "metric_operand" in value:
        import capo_quicksight.types.identifier

        out["MetricOperand"] = capo_quicksight.types.identifier.serialize_json(
            value["metric_operand"]
        )
    if "function" in value:
        import capo_quicksight.types.agg_type

        out["Function"] = capo_quicksight.types.agg_type.serialize_json(
            value["function"]
        )
    if "sort_direction" in value:
        import capo_quicksight.types.topic_sort_direction

        out["SortDirection"] = (
            capo_quicksight.types.topic_sort_direction.serialize_json(
                value["sort_direction"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterAggMetrics:
    out: FilterAggMetrics = {}  # type: ignore[typeddict-item]
    if "MetricOperand" in data:
        import capo_quicksight.types.identifier

        out["metric_operand"] = capo_quicksight.types.identifier.deserialize_json(
            data["MetricOperand"]
        )
    if "Function" in data:
        import capo_quicksight.types.agg_type

        out["function"] = capo_quicksight.types.agg_type.deserialize_json(
            data["Function"]
        )
    if "SortDirection" in data:
        import capo_quicksight.types.topic_sort_direction

        out["sort_direction"] = (
            capo_quicksight.types.topic_sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    return out
