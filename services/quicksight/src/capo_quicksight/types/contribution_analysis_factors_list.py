"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisFactorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.contribution_analysis_factor

ContributionAnalysisFactorsList: TypeAlias = list[
    "capo_quicksight.types.contribution_analysis_factor.ContributionAnalysisFactor"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisFactorsList) -> list:
    import capo_quicksight.types.contribution_analysis_factor

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.contribution_analysis_factor.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContributionAnalysisFactorsList:
    import capo_quicksight.types.contribution_analysis_factor

    out: ContributionAnalysisFactorsList = []
    for item in data:
        out.append(
            capo_quicksight.types.contribution_analysis_factor.deserialize_json(item)
        )
    return out
