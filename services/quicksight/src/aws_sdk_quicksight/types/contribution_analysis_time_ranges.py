"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisTimeRanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.topic_ir_filter_option


class ContributionAnalysisTimeRanges(TypedDict, closed=True):
    start_range: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_filter_option.TopicIRFilterOption"
    ]
    """<p>The start range for the <code>ContributionAnalysisTimeRanges</code>.</p>"""
    end_range: NotRequired[
        "aws_sdk_quicksight.types.topic_ir_filter_option.TopicIRFilterOption"
    ]
    """<p>The end range for the <code>ContributionAnalysisTimeRanges</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisTimeRanges) -> dict:
    out: dict = {}
    if "start_range" in value:
        import aws_sdk_quicksight.types.topic_ir_filter_option

        out["StartRange"] = (
            aws_sdk_quicksight.types.topic_ir_filter_option.serialize_json(
                value["start_range"]
            )
        )
    if "end_range" in value:
        import aws_sdk_quicksight.types.topic_ir_filter_option

        out["EndRange"] = (
            aws_sdk_quicksight.types.topic_ir_filter_option.serialize_json(
                value["end_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContributionAnalysisTimeRanges:
    out: ContributionAnalysisTimeRanges = {}  # type: ignore[typeddict-item]
    if "StartRange" in data:
        import aws_sdk_quicksight.types.topic_ir_filter_option

        out["start_range"] = (
            aws_sdk_quicksight.types.topic_ir_filter_option.deserialize_json(
                data["StartRange"]
            )
        )
    if "EndRange" in data:
        import aws_sdk_quicksight.types.topic_ir_filter_option

        out["end_range"] = (
            aws_sdk_quicksight.types.topic_ir_filter_option.deserialize_json(
                data["EndRange"]
            )
        )
    return out
