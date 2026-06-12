"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Thumbnail type."""
ThumbnailType: TypeAlias = Literal[
    "UNSPECIFIED",
    "CURRENT_ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNSPECIFIED",
        "CURRENT_ACTIVE",
    )
)


def serialize_json(value: ThumbnailType) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThumbnailType value: {data!r}")
    return cast(ThumbnailType, data)
