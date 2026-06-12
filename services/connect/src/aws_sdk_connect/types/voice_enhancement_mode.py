"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

VoiceEnhancementMode: TypeAlias = Literal[
    "VOICE_ISOLATION",
    "NOISE_SUPPRESSION",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOICE_ISOLATION",
        "NOISE_SUPPRESSION",
        "NONE",
    )
)


def serialize_json(value: VoiceEnhancementMode) -> str:
    return value


def deserialize_json(data: str) -> VoiceEnhancementMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VoiceEnhancementMode value: {data!r}")
    return cast(VoiceEnhancementMode, data)
