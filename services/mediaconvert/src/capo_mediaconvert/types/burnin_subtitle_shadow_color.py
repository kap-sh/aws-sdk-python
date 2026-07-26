"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleShadowColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the color of the shadow cast by the captions. Leave Shadow color blank and set Style passthrough to enabled to use the shadow color data from your input captions, if present."""
BurninSubtitleShadowColor: TypeAlias = Literal[
    "NONE",
    "BLACK",
    "WHITE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurninSubtitleShadowColor) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleShadowColor:
    return cast(BurninSubtitleShadowColor, data)
