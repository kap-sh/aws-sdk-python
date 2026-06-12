"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2CodecLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Level to set the MPEG-2 level for the video output."""
Mpeg2CodecLevel: TypeAlias = Literal[
    "AUTO",
    "LOW",
    "MAIN",
    "HIGH1440",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "LOW",
        "MAIN",
        "HIGH1440",
        "HIGH",
    )
)


def serialize_json(value: Mpeg2CodecLevel) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2CodecLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2CodecLevel value: {data!r}")
    return cast(Mpeg2CodecLevel, data)
