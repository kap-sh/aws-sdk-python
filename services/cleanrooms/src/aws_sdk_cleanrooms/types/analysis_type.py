"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisType``."""

from typing import Literal, TypeAlias, cast

AnalysisType: TypeAlias = Literal[
    "DIRECT_ANALYSIS",
    "ADDITIONAL_ANALYSIS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisType) -> str:
    return value


def deserialize_json(data: str) -> AnalysisType:
    return cast(AnalysisType, data)
