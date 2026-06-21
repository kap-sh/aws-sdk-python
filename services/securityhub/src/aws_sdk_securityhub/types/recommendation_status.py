"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
