"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRComparisonMethod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.comparison_method_type
    import aws_sdk_quicksight.types.integer
    import aws_sdk_quicksight.types.topic_time_granularity


class TopicIRComparisonMethod(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_quicksight.types.comparison_method_type.ComparisonMethodType"
    ]
    """<p>The type for the <code>TopicIRComparisonMethod</code>.</p>"""
    period: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The period for the <code>TopicIRComparisonMethod</code>.</p>"""
    window_size: "aws_sdk_quicksight.types.integer.Integer"
    """<p>The window size for the <code>TopicIRComparisonMethod</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRComparisonMethod) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_quicksight.types.comparison_method_type

        out["Type"] = aws_sdk_quicksight.types.comparison_method_type.serialize_json(
            value["type"]
        )
    if "period" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["Period"] = aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
            value["period"]
        )
    out["WindowSize"] = value.get("window_size", 0)
    return out


def deserialize_json(data: dict) -> TopicIRComparisonMethod:
    out: TopicIRComparisonMethod = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_quicksight.types.comparison_method_type

        out["type"] = aws_sdk_quicksight.types.comparison_method_type.deserialize_json(
            data["Type"]
        )
    if "Period" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["period"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["Period"]
            )
        )
    if "WindowSize" in data:
        out["window_size"] = data["WindowSize"]
    else:
        out["window_size"] = 0
    return out
