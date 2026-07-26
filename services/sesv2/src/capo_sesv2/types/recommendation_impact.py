"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationImpact``."""

from typing import Literal, TypeAlias, cast

RecommendationImpact: TypeAlias = Literal[
    "LOW",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationImpact) -> str:
    return value


def deserialize_json(data: str) -> RecommendationImpact:
    return cast(RecommendationImpact, data)
