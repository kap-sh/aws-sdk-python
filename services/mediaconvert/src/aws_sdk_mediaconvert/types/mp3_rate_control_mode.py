"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp3RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR)."""
Mp3RateControlMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CBR",
        "VBR",
    )
)


def serialize_json(value: Mp3RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Mp3RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mp3RateControlMode value: {data!r}")
    return cast(Mp3RateControlMode, data)
