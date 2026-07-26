"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantRecordingMediaType``."""

from typing import Literal, TypeAlias, cast

ParticipantRecordingMediaType: TypeAlias = Literal[
    "AUDIO_VIDEO",
    "AUDIO_ONLY",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantRecordingMediaType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantRecordingMediaType:
    return cast(ParticipantRecordingMediaType, data)
