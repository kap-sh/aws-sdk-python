"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisFactorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.contribution_analysis_factor

ContributionAnalysisFactorsList: TypeAlias = list[
    "aws_sdk_quicksight.types.contribution_analysis_factor.ContributionAnalysisFactor"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisFactorsList) -> list:
    import aws_sdk_quicksight.types.contribution_analysis_factor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.contribution_analysis_factor.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContributionAnalysisFactorsList:
    import aws_sdk_quicksight.types.contribution_analysis_factor

    out: ContributionAnalysisFactorsList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.contribution_analysis_factor.deserialize_json(item)
        )
    return out
