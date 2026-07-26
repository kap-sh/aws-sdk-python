"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleFontColor``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: DvbSubtitleFontColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleFontColor:
    return cast(DvbSubtitleFontColor, data)
