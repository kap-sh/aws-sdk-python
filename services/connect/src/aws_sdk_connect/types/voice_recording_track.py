"""Generated from Smithy shape ``com.amazonaws.connect#VoiceRecordingTrack``."""

from typing import Literal, TypeAlias, cast

VoiceRecordingTrack: TypeAlias = Literal[
    "FROM_AGENT",
    "TO_AGENT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceRecordingTrack) -> str:
    return value


def deserialize_json(data: str) -> VoiceRecordingTrack:
    return cast(VoiceRecordingTrack, data)
