"""Generated from Smithy shape ``com.amazonaws.connect#VoiceRecordingTrack``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

VoiceRecordingTrack: TypeAlias = Literal[
    "FROM_AGENT",
    "TO_AGENT",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FROM_AGENT",
        "TO_AGENT",
        "ALL",
    )
)


def serialize_json(value: VoiceRecordingTrack) -> str:
    return value


def deserialize_json(data: str) -> VoiceRecordingTrack:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VoiceRecordingTrack value: {data!r}")
    return cast(VoiceRecordingTrack, data)
