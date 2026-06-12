"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedSlowPal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output by relabeling the video frames and resampling your audio. Note that enabling this setting will slightly reduce the duration of your video. Related settings: You must also set Framerate to 25."""
UncompressedSlowPal: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: UncompressedSlowPal) -> str:
    return value


def deserialize_json(data: str) -> UncompressedSlowPal:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UncompressedSlowPal value: {data!r}")
    return cast(UncompressedSlowPal, data)
