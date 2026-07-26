"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRContributionAnalysis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.contribution_analysis_direction
    import capo_quicksight.types.contribution_analysis_factors_list
    import capo_quicksight.types.contribution_analysis_sort_type
    import capo_quicksight.types.contribution_analysis_time_ranges


class TopicIRContributionAnalysis(TypedDict, closed=True):
    factors: NotRequired[
        "capo_quicksight.types.contribution_analysis_factors_list.ContributionAnalysisFactorsList"
    ]
    """<p>The factors for a <code>TopicIRContributionAnalysis</code>.</p>"""
    time_ranges: NotRequired[
        "capo_quicksight.types.contribution_analysis_time_ranges.ContributionAnalysisTimeRanges"
    ]
    """<p>The time ranges for the <code>TopicIRContributionAnalysis</code>.</p>"""
    direction: NotRequired[
        "capo_quicksight.types.contribution_analysis_direction.ContributionAnalysisDirection"
    ]
    """<p>The direction for the <code>TopicIRContributionAnalysis</code>.</p>"""
    sort_type: NotRequired[
        "capo_quicksight.types.contribution_analysis_sort_type.ContributionAnalysisSortType"
    ]
    """<p>The sort type for the <code>TopicIRContributionAnalysis</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRContributionAnalysis) -> dict:
    out: dict = {}
    if "factors" in value:
        import capo_quicksight.types.contribution_analysis_factors_list

        out["Factors"] = (
            capo_quicksight.types.contribution_analysis_factors_list.serialize_json(
                value["factors"]
            )
        )
    if "time_ranges" in value:
        import capo_quicksight.types.contribution_analysis_time_ranges

        out["TimeRanges"] = (
            capo_quicksight.types.contribution_analysis_time_ranges.serialize_json(
                value["time_ranges"]
            )
        )
    if "direction" in value:
        import capo_quicksight.types.contribution_analysis_direction

        out["Direction"] = (
            capo_quicksight.types.contribution_analysis_direction.serialize_json(
                value["direction"]
            )
        )
    if "sort_type" in value:
        import capo_quicksight.types.contribution_analysis_sort_type

        out["SortType"] = (
            capo_quicksight.types.contribution_analysis_sort_type.serialize_json(
                value["sort_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicIRContributionAnalysis:
    out: TopicIRContributionAnalysis = {}  # type: ignore[typeddict-item]
    if "Factors" in data:
        import capo_quicksight.types.contribution_analysis_factors_list

        out["factors"] = (
            capo_quicksight.types.contribution_analysis_factors_list.deserialize_json(
                data["Factors"]
            )
        )
    if "TimeRanges" in data:
        import capo_quicksight.types.contribution_analysis_time_ranges

        out["time_ranges"] = (
            capo_quicksight.types.contribution_analysis_time_ranges.deserialize_json(
                data["TimeRanges"]
            )
        )
    if "Direction" in data:
        import capo_quicksight.types.contribution_analysis_direction

        out["direction"] = (
            capo_quicksight.types.contribution_analysis_direction.deserialize_json(
                data["Direction"]
            )
        )
    if "SortType" in data:
        import capo_quicksight.types.contribution_analysis_sort_type

        out["sort_type"] = (
            capo_quicksight.types.contribution_analysis_sort_type.deserialize_json(
                data["SortType"]
            )
        )
    return out
