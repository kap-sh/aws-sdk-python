"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsEbpPlacement``."""

from typing import Literal, TypeAlias, cast

"""Selects which PIDs to place EBP markers on. They can either be placed only on the video PID, or on both the video PID and all audio PIDs. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY)."""
M2tsEbpPlacement: TypeAlias = Literal[
    "VIDEO_AND_AUDIO_PIDS",
    "VIDEO_PID",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEbpPlacement) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbpPlacement:
    return cast(M2tsEbpPlacement, data)
