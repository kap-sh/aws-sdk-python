"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRContributionAnalysis``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.contribution_analysis_direction
    import aws_sdk_quicksight.types.contribution_analysis_factors_list
    import aws_sdk_quicksight.types.contribution_analysis_sort_type
    import aws_sdk_quicksight.types.contribution_analysis_time_ranges


class TopicIRContributionAnalysis(TypedDict):
    factors: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_factors_list.ContributionAnalysisFactorsList"
    ]
    """<p>The factors for a <code>TopicIRContributionAnalysis</code>.</p>"""
    time_ranges: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_time_ranges.ContributionAnalysisTimeRanges"
    ]
    """<p>The time ranges for the <code>TopicIRContributionAnalysis</code>.</p>"""
    direction: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_direction.ContributionAnalysisDirection"
    ]
    """<p>The direction for the <code>TopicIRContributionAnalysis</code>.</p>"""
    sort_type: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_sort_type.ContributionAnalysisSortType"
    ]
    """<p>The sort type for the <code>TopicIRContributionAnalysis</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRContributionAnalysis) -> dict:
    out: dict = {}
    if "factors" in value:
        import aws_sdk_quicksight.types.contribution_analysis_factors_list

        out["Factors"] = (
            aws_sdk_quicksight.types.contribution_analysis_factors_list.serialize_json(
                value["factors"]
            )
        )
    if "time_ranges" in value:
        import aws_sdk_quicksight.types.contribution_analysis_time_ranges

        out["TimeRanges"] = (
            aws_sdk_quicksight.types.contribution_analysis_time_ranges.serialize_json(
                value["time_ranges"]
            )
        )
    if "direction" in value:
        import aws_sdk_quicksight.types.contribution_analysis_direction

        out["Direction"] = (
            aws_sdk_quicksight.types.contribution_analysis_direction.serialize_json(
                value["direction"]
            )
        )
    if "sort_type" in value:
        import aws_sdk_quicksight.types.contribution_analysis_sort_type

        out["SortType"] = (
            aws_sdk_quicksight.types.contribution_analysis_sort_type.serialize_json(
                value["sort_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicIRContributionAnalysis:
    out: TopicIRContributionAnalysis = {}  # type: ignore[typeddict-item]
    if "Factors" in data:
        import aws_sdk_quicksight.types.contribution_analysis_factors_list

        out["factors"] = (
            aws_sdk_quicksight.types.contribution_analysis_factors_list.deserialize_json(
                data["Factors"]
            )
        )
    if "TimeRanges" in data:
        import aws_sdk_quicksight.types.contribution_analysis_time_ranges

        out["time_ranges"] = (
            aws_sdk_quicksight.types.contribution_analysis_time_ranges.deserialize_json(
                data["TimeRanges"]
            )
        )
    if "Direction" in data:
        import aws_sdk_quicksight.types.contribution_analysis_direction

        out["direction"] = (
            aws_sdk_quicksight.types.contribution_analysis_direction.deserialize_json(
                data["Direction"]
            )
        )
    if "SortType" in data:
        import aws_sdk_quicksight.types.contribution_analysis_sort_type

        out["sort_type"] = (
            aws_sdk_quicksight.types.contribution_analysis_sort_type.deserialize_json(
                data["SortType"]
            )
        )
    return out
