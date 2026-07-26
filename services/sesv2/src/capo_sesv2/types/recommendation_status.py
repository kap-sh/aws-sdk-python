"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationStatus: TypeAlias = Literal[
    "OPEN",
    "FIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
