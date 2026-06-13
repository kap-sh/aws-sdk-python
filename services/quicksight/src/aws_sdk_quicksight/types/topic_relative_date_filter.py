"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRelativeDateFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_relative_date_filter_function
    import aws_sdk_quicksight.types.topic_singular_filter_constant
    import aws_sdk_quicksight.types.topic_time_granularity


class TopicRelativeDateFilter(TypedDict):
    time_granularity: NotRequired[
        "aws_sdk_quicksight.types.topic_time_granularity.TopicTimeGranularity"
    ]
    """<p>The level of time precision that is used to aggregate <code>DateTime</code> values.</p>"""
    relative_date_filter_function: NotRequired[
        "aws_sdk_quicksight.types.topic_relative_date_filter_function.TopicRelativeDateFilterFunction"
    ]
    """<p>The function to be used in a relative date filter to determine the range of dates to include in the results. Valid values for this structure are <code>BEFORE</code>, <code>AFTER</code>, and <code>BETWEEN</code>.</p>"""
    constant: NotRequired[
        "aws_sdk_quicksight.types.topic_singular_filter_constant.TopicSingularFilterConstant"
    ]
    """<p>The constant used in a relative date filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRelativeDateFilter) -> dict:
    out: dict = {}
    if "time_granularity" in value:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["TimeGranularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.serialize_json(
                value["time_granularity"]
            )
        )
    if "relative_date_filter_function" in value:
        import aws_sdk_quicksight.types.topic_relative_date_filter_function

        out["RelativeDateFilterFunction"] = (
            aws_sdk_quicksight.types.topic_relative_date_filter_function.serialize_json(
                value["relative_date_filter_function"]
            )
        )
    if "constant" in value:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["Constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.serialize_json(
                value["constant"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRelativeDateFilter:
    out: TopicRelativeDateFilter = {}  # type: ignore[typeddict-item]
    if "TimeGranularity" in data:
        import aws_sdk_quicksight.types.topic_time_granularity

        out["time_granularity"] = (
            aws_sdk_quicksight.types.topic_time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    if "RelativeDateFilterFunction" in data:
        import aws_sdk_quicksight.types.topic_relative_date_filter_function

        out["relative_date_filter_function"] = (
            aws_sdk_quicksight.types.topic_relative_date_filter_function.deserialize_json(
                data["RelativeDateFilterFunction"]
            )
        )
    if "Constant" in data:
        import aws_sdk_quicksight.types.topic_singular_filter_constant

        out["constant"] = (
            aws_sdk_quicksight.types.topic_singular_filter_constant.deserialize_json(
                data["Constant"]
            )
        )
    return out
