"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationStatus: TypeAlias = Literal[
    "Implemented",
    "Inactive",
    "NotImplemented",
    "Excluded",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
