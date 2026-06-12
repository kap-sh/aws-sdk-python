"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantRecordingMediaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

ParticipantRecordingMediaType: TypeAlias = Literal[
    "AUDIO_VIDEO",
    "AUDIO_ONLY",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO_VIDEO",
        "AUDIO_ONLY",
        "NONE",
    )
)


def serialize_json(value: ParticipantRecordingMediaType) -> str:
    return value


def deserialize_json(data: str) -> ParticipantRecordingMediaType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ParticipantRecordingMediaType value: {data!r}"
        )
    return cast(ParticipantRecordingMediaType, data)
