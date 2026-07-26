"""Generated from Smithy shape ``com.amazonaws.quicksight#AnalysisFilterAttribute``."""

from typing import Literal, TypeAlias, cast

AnalysisFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_USER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "ANALYSIS_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> AnalysisFilterAttribute:
    return cast(AnalysisFilterAttribute, data)
