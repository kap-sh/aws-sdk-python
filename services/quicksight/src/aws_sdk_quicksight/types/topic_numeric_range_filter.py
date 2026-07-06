"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNumericRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean
    import aws_sdk_quicksight.types.named_filter_agg_type
    import aws_sdk_quicksight.types.topic_range_filter_constant


class TopicNumericRangeFilter(TypedDict, closed=True):
    inclusive: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether the endpoints of the numeric range are included in the filter. If set to true, topics whose numeric field value is equal to the endpoint values will be included in the filter. If set to false, topics whose numeric field value is equal to the endpoint values will be excluded from the filter.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_range_filter_constant.TopicRangeFilterConstant"
    ]
    """<p>The constant used in a numeric range filter.</p>"""
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.named_filter_agg_type.NamedFilterAggType"
    ]
    """<p>An aggregation function that specifies how to calculate the value of a numeric field for a topic, Valid values for this structure are <code>NO_AGGREGATION</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>MIN</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, and <code>VARP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNumericRangeFilter) -> dict:
    out: dict = {}
    out["Inclusive"] = value.get("inclusive", False)
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_range_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_range_filter_constant.serialize_json(
                value["constant"]
            )
        )
    if "aggregation" in value:
        import aws_sdk_quicksight.types.named_filter_agg_type

        out["Aggregation"] = (
            aws_sdk_quicksight.types.named_filter_agg_type.serialize_json(
                value["aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicNumericRangeFilter:
    out: TopicNumericRangeFilter = {}  # type: ignore[typeddict-item]
    if "Inclusive" in data:
        out["inclusive"] = data["Inclusive"]
    else:
        out["inclusive"] = False
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_range_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_range_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    if "Aggregation" in data:
        import aws_sdk_quicksight.types.named_filter_agg_type

        out["aggregation"] = (
            aws_sdk_quicksight.types.named_filter_agg_type.deserialize_json(
                data["Aggregation"]
            )
        )
    return out
