"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

RecommendationStatus: TypeAlias = Literal[
    "ok",
    "warning",
    "error",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ok",
        "warning",
        "error",
    )
)


def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
