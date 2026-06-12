"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleOutlineColor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present. Within your job settings, all of your DVB-Sub settings must be identical."""
DvbSubtitleOutlineColor: TypeAlias = Literal[
    "BLACK",
    "WHITE",
    "YELLOW",
    "RED",
    "GREEN",
    "BLUE",
    "AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLACK",
        "WHITE",
        "YELLOW",
        "RED",
        "GREEN",
        "BLUE",
        "AUTO",
    )
)


def serialize_json(value: DvbSubtitleOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleOutlineColor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DvbSubtitleOutlineColor value: {data!r}")
    return cast(DvbSubtitleOutlineColor, data)
