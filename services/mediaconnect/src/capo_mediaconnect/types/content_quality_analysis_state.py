"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ContentQualityAnalysisState``."""

from typing import Literal, TypeAlias, cast

ContentQualityAnalysisState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentQualityAnalysisState) -> str:
    return value


def deserialize_json(data: str) -> ContentQualityAnalysisState:
    return cast(ContentQualityAnalysisState, data)
