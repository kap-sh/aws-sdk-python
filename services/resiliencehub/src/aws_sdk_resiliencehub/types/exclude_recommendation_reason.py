"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ExcludeRecommendationReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ExcludeRecommendationReason: TypeAlias = Literal[
    "AlreadyImplemented",
    "NotRelevant",
    "ComplexityOfImplementation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AlreadyImplemented",
        "NotRelevant",
        "ComplexityOfImplementation",
    )
)


def serialize_json(value: ExcludeRecommendationReason) -> str:
    return value


def deserialize_json(data: str) -> ExcludeRecommendationReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExcludeRecommendationReason value: {data!r}"
        )
    return cast(ExcludeRecommendationReason, data)
