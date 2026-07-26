"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsEbpAudioInterval``."""

from typing import Literal, TypeAlias, cast

"""When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY)."""
M2tsEbpAudioInterval: TypeAlias = Literal[
    "VIDEO_AND_FIXED_INTERVALS",
    "VIDEO_INTERVAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEbpAudioInterval) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbpAudioInterval:
    return cast(M2tsEbpAudioInterval, data)
