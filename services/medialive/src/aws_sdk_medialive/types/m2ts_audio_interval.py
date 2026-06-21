"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAudioInterval``."""

from typing import Literal, TypeAlias, cast

"""M2ts Audio Interval"""
M2tsAudioInterval: TypeAlias = Literal[
    "VIDEO_AND_FIXED_INTERVALS",
    "VIDEO_INTERVAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAudioInterval) -> str:
    return value


def deserialize_json(data: str) -> M2tsAudioInterval:
    return cast(M2tsAudioInterval, data)
