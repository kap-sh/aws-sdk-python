"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationImpact``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

RecommendationImpact: TypeAlias = Literal[
    "LOW",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "HIGH",
    )
)


def serialize_json(value: RecommendationImpact) -> str:
    return value


def deserialize_json(data: str) -> RecommendationImpact:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationImpact value: {data!r}")
    return cast(RecommendationImpact, data)
