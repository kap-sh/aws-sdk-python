"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderRecipeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RecommenderRecipeName: TypeAlias = Literal[
    "recommended-for-you",
    "similar-items",
    "frequently-paired-items",
    "popular-items",
    "trending-now",
    "personalized-ranking",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "recommended-for-you",
        "similar-items",
        "frequently-paired-items",
        "popular-items",
        "trending-now",
        "personalized-ranking",
    )
)


def serialize_json(value: RecommenderRecipeName) -> str:
    return value


def deserialize_json(data: str) -> RecommenderRecipeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommenderRecipeName value: {data!r}")
    return cast(RecommenderRecipeName, data)
