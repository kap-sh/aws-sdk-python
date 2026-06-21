"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupAudioOnlyTimecodeControl``."""

from typing import Literal, TypeAlias, cast

"""Smooth Group Audio Only Timecode Control"""
SmoothGroupAudioOnlyTimecodeControl: TypeAlias = Literal[
    "PASSTHROUGH",
    "USE_CONFIGURED_CLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmoothGroupAudioOnlyTimecodeControl) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupAudioOnlyTimecodeControl:
    return cast(SmoothGroupAudioOnlyTimecodeControl, data)
