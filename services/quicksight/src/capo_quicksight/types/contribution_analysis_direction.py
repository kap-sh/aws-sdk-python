"""Generated from Smithy shape ``com.amazonaws.quicksight#ContributionAnalysisDirection``."""

from typing import Literal, TypeAlias, cast

ContributionAnalysisDirection: TypeAlias = Literal[
    "INCREASE",
    "DECREASE",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContributionAnalysisDirection) -> str:
    return value


def deserialize_json(data: str) -> ContributionAnalysisDirection:
    return cast(ContributionAnalysisDirection, data)
