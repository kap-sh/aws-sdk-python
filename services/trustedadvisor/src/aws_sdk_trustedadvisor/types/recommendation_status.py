"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationStatus: TypeAlias = Literal[
    "ok",
    "warning",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
