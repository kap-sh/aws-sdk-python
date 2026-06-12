"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2RateControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr)."""
Mpeg2RateControlMode: TypeAlias = Literal[
    "VBR",
    "CBR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VBR",
        "CBR",
    )
)


def serialize_json(value: Mpeg2RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2RateControlMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2RateControlMode value: {data!r}")
    return cast(Mpeg2RateControlMode, data)
