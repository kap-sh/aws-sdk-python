"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleFontColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the color of the captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical."""
DvbSubtitleFontColor: TypeAlias = Literal[
    "WHITE",
    "BLACK",
    "YELLOW",
    "RED",
    "GREEN",
    "BLUE",
    "HEX",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WHITE",
        "BLACK",
        "YELLOW",
        "RED",
        "GREEN",
        "BLUE",
        "HEX",
        "AUTO",
    )
)


def serialize_json(value: DvbSubtitleFontColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleFontColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitleFontColor value: {data!r}")
    return cast(DvbSubtitleFontColor, data)
