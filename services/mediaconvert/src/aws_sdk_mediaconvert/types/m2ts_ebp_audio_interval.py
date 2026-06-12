"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsEbpAudioInterval``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to VIDEO_AND_FIXED_INTERVALS, audio EBP markers will be added to partitions 3 and 4. The interval between these additional markers will be fixed, and will be slightly shorter than the video EBP marker interval. When set to VIDEO_INTERVAL, these additional markers will not be inserted. Only applicable when EBP segmentation markers are is selected (segmentationMarkers is EBP or EBP_LEGACY)."""
M2tsEbpAudioInterval: TypeAlias = Literal[
    "VIDEO_AND_FIXED_INTERVALS",
    "VIDEO_INTERVAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIDEO_AND_FIXED_INTERVALS",
        "VIDEO_INTERVAL",
    )
)


def serialize_json(value: M2tsEbpAudioInterval) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbpAudioInterval:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsEbpAudioInterval value: {data!r}")
    return cast(M2tsEbpAudioInterval, data)
