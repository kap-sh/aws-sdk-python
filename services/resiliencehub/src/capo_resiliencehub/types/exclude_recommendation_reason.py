"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ExcludeRecommendationReason``."""

from typing import Literal, TypeAlias, cast

ExcludeRecommendationReason: TypeAlias = Literal[
    "AlreadyImplemented",
    "NotRelevant",
    "ComplexityOfImplementation",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludeRecommendationReason) -> str:
    return value


def deserialize_json(data: str) -> ExcludeRecommendationReason:
    return cast(ExcludeRecommendationReason, data)
