"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoOverlayPlayBackMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether your video overlay repeats or plays only once. To repeat your video overlay on a loop: Keep the default value, Repeat. Your overlay will repeat for the duration of the base input video. To playback your video overlay only once: Choose Once. With either option, you can end playback at a time that you specify by entering a value for End timecode."""
VideoOverlayPlayBackMode: TypeAlias = Literal[
    "ONCE",
    "REPEAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONCE",
        "REPEAT",
    )
)


def serialize_json(value: VideoOverlayPlayBackMode) -> str:
    return value


def deserialize_json(data: str) -> VideoOverlayPlayBackMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoOverlayPlayBackMode value: {data!r}")
    return cast(VideoOverlayPlayBackMode, data)
