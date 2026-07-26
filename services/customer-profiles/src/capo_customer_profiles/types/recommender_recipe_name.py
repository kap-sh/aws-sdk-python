"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderRecipeName``."""

from typing import Literal, TypeAlias, cast

RecommenderRecipeName: TypeAlias = Literal[
    "recommended-for-you",
    "similar-items",
    "frequently-paired-items",
    "popular-items",
    "trending-now",
    "personalized-ranking",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommenderRecipeName) -> str:
    return value


def deserialize_json(data: str) -> RecommenderRecipeName:
    return cast(RecommenderRecipeName, data)
