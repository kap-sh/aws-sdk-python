"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265SlowPal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25."""
H265SlowPal: TypeAlias = Literal[
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


def serialize_json(value: H265SlowPal) -> str:
    return value


def deserialize_json(data: str) -> H265SlowPal:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265SlowPal value: {data!r}")
    return cast(H265SlowPal, data)
