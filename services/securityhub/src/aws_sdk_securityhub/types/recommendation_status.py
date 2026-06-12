"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RecommendationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
