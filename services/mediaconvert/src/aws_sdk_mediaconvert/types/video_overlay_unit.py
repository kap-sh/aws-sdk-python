"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayUnit``."""

from typing import Literal, TypeAlias, cast

"""Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels."""
VideoOverlayUnit: TypeAlias = Literal[
    "PIXELS",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoOverlayUnit) -> str:
    return value


def deserialize_json(data: str) -> VideoOverlayUnit:
    return cast(VideoOverlayUnit, data)
