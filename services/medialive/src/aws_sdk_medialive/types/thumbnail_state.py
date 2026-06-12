"""Generated from Smithy shape ``com.amazonaws.medialive#ThumbnailState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Thumbnail State"""
ThumbnailState: TypeAlias = Literal[
    "AUTO",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "DISABLED",
    )
)


def serialize_json(value: ThumbnailState) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThumbnailState value: {data!r}")
    return cast(ThumbnailState, data)
