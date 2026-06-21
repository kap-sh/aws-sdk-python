"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleFontColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the color of the burned-in captions text. Leave Font color blank and set Style passthrough to enabled to use the font color data from your input captions, if present."""
BurninSubtitleFontColor: TypeAlias = Literal[
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
def serialize_json(value: BurninSubtitleFontColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleFontColor:
    return cast(BurninSubtitleFontColor, data)
