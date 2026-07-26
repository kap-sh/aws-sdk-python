"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PlaybackInterruptionReason``."""

from typing import Literal, TypeAlias, cast

PlaybackInterruptionReason: TypeAlias = Literal[
    "DTMF_START_DETECTED",
    "TEXT_DETECTED",
    "VOICE_START_DETECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackInterruptionReason) -> str:
    return value


def deserialize_json(data: str) -> PlaybackInterruptionReason:
    return cast(PlaybackInterruptionReason, data)
