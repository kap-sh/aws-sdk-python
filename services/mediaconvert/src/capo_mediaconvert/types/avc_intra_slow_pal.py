"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraSlowPal``."""

from typing import Literal, TypeAlias, cast

"""Ignore this setting unless your input frame rate is 23.976 or 24 frames per second (fps). Enable slow PAL to create a 25 fps output. When you enable slow PAL, MediaConvert relabels the video frames to 25 fps and resamples your audio to keep it synchronized with the video. Note that enabling this setting will slightly reduce the duration of your video. Required settings: You must also set Framerate to 25."""
AvcIntraSlowPal: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AvcIntraSlowPal) -> str:
    return value


def deserialize_json(data: str) -> AvcIntraSlowPal:
    return cast(AvcIntraSlowPal, data)
