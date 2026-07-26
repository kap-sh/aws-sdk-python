"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleBackgroundColor``."""

from typing import Literal, TypeAlias, cast

"""Specify the color of the rectangle behind the captions. Leave background color blank and set Style passthrough to enabled to use the background color data from your input captions, if present."""
DvbSubtitleBackgroundColor: TypeAlias = Literal[
    "NONE",
    "BLACK",
    "WHITE",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubtitleBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleBackgroundColor:
    return cast(DvbSubtitleBackgroundColor, data)
