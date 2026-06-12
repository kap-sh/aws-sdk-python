"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#PlaybackInterruptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

PlaybackInterruptionReason: TypeAlias = Literal[
    "DTMF_START_DETECTED",
    "TEXT_DETECTED",
    "VOICE_START_DETECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DTMF_START_DETECTED",
        "TEXT_DETECTED",
        "VOICE_START_DETECTED",
    )
)


def serialize_json(value: PlaybackInterruptionReason) -> str:
    return value


def deserialize_json(data: str) -> PlaybackInterruptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PlaybackInterruptionReason value: {data!r}"
        )
    return cast(PlaybackInterruptionReason, data)
