"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the Unit type to use when you enter a value for X position, Y position, Width, or Height. You can choose Pixels or Percentage. Leave blank to use the default value, Pixels."""
VideoOverlayUnit: TypeAlias = Literal[
    "PIXELS",
    "PERCENTAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PIXELS",
        "PERCENTAGE",
    )
)


def serialize_json(value: VideoOverlayUnit) -> str:
    return value


def deserialize_json(data: str) -> VideoOverlayUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoOverlayUnit value: {data!r}")
    return cast(VideoOverlayUnit, data)
