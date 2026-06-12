"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4FreeSpaceBox``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Inserts a free-space box immediately after the moov box."""
Mp4FreeSpaceBox: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: Mp4FreeSpaceBox) -> str:
    return value


def deserialize_json(data: str) -> Mp4FreeSpaceBox:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mp4FreeSpaceBox value: {data!r}")
    return cast(Mp4FreeSpaceBox, data)
