"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PadVideo``."""

from typing import Literal, TypeAlias, cast

"""Use this setting if your input has video and audio durations that don't align, and your output or player has strict alignment requirements. Examples: Input audio track has a delayed start. Input video track ends before audio ends. When you set Pad video to Black, MediaConvert generates black video frames so that output video and audio durations match. Black video frames are added at the beginning or end, depending on your input. To keep the default behavior and not generate black video, set Pad video to Disabled or leave blank."""
PadVideo: TypeAlias = Literal[
    "DISABLED",
    "BLACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: PadVideo) -> str:
    return value


def deserialize_json(data: str) -> PadVideo:
    return cast(PadVideo, data)
