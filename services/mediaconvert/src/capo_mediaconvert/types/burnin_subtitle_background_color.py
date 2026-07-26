"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleBackgroundColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present."""
BurninSubtitleBackgroundColor: TypeAlias = Literal[
    "NONE",
    "BLACK",
    "WHITE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurninSubtitleBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleBackgroundColor:
    return cast(BurninSubtitleBackgroundColor, data)
