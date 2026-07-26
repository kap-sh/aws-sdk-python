"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleOutlineColor``."""

from typing import Literal, TypeAlias, cast

"""Specify font outline color. Leave Outline color blank and set Style passthrough to enabled to use the font outline color data from your input captions, if present."""
BurninSubtitleOutlineColor: TypeAlias = Literal[
    "BLACK",
    "WHITE",
    "YELLOW",
    "RED",
    "GREEN",
    "BLUE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurninSubtitleOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleOutlineColor:
    return cast(BurninSubtitleOutlineColor, data)
