"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNumericEqualityFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.named_filter_agg_type
    import aws_sdk_quicksight.types.topic_singular_filter_constant


class TopicNumericEqualityFilter(TypedDict):
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    """<p>The constant used in a numeric equality filter.</p>"""
    aggregation: NotRequired[
        "aws_sdk_quicksight.types.named_filter_agg_type.NamedFilterAggType"
    ]
    """<p>An aggregation function that specifies how to calculate the value of a numeric field for a topic. Valid values for this structure are <code>NO_AGGREGATION</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>COUNT</code>, <code>DISTINCT_COUNT</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>MIN</code>, <code>STDEV</code>, <code>STDEVP</code>, <code>VAR</code>, and <code>VARP</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNumericEqualityFilter) -> dict:
    out: dict = {}
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.serialize_json(
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


def deserialize_json(data: dict) -> TopicNumericEqualityFilter:
    out: TopicNumericEqualityFilter = {}  # type: ignore[typeddict-item]
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.deserialize_json(
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
