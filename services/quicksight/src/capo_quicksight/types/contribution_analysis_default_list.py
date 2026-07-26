"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisDefaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.contribution_analysis_default

ContributionAnalysisDefaultList: TypeAlias = list[
    "capo_quicksight.types.contribution_analysis_default.ContributionAnalysisDefault"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisDefaultList) -> list:
    import capo_quicksight.types.contribution_analysis_default

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.contribution_analysis_default.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContributionAnalysisDefaultList:
    import capo_quicksight.types.contribution_analysis_default

    out: ContributionAnalysisDefaultList = []
    for item in data:
        out.append(
            capo_quicksight.types.contribution_analysis_default.deserialize_json(item)
        )
    return out
