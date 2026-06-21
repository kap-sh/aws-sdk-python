"""Generated from Smithy shape ``com.amazonaws.mediaconvert#BurninSubtitleTeletextSpacing``."""

from typing import Literal, TypeAlias, cast

"""Specify whether the text spacing in your captions is set by the captions grid, or varies depending on letter width. Choose fixed grid to conform to the spacing specified in the captions file more accurately. Choose proportional to make the text easier to read for closed captions."""
BurninSubtitleTeletextSpacing: TypeAlias = Literal[
    "FIXED_GRID",
    "PROPORTIONAL",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurninSubtitleTeletextSpacing) -> str:
    return value


def deserialize_json(data: str) -> BurninSubtitleTeletextSpacing:
    return cast(BurninSubtitleTeletextSpacing, data)
