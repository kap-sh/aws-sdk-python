"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

RecommendationStatus: TypeAlias = Literal[
    "Implemented",
    "Inactive",
    "NotImplemented",
    "Excluded",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Implemented",
        "Inactive",
        "NotImplemented",
        "Excluded",
    )
)


def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationStatus value: {data!r}")
    return cast(RecommendationStatus, data)
