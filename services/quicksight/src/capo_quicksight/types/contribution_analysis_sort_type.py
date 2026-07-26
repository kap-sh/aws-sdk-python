"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisSortType``."""

from typing import Literal, TypeAlias, cast

ContributionAnalysisSortType: TypeAlias = Literal[
    "ABSOLUTE_DIFFERENCE",
    "CONTRIBUTION_PERCENTAGE",
    "DEVIATION_FROM_EXPECTED",
    "PERCENTAGE_DIFFERENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisSortType) -> str:
    return value


def deserialize_json(data: str) -> ContributionAnalysisSortType:
    return cast(ContributionAnalysisSortType, data)
