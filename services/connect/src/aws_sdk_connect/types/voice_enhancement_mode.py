"""Generated from Smithy shape ``com.amazonaws.connect#VoiceEnhancementMode``."""

from typing import Literal, TypeAlias, cast

VoiceEnhancementMode: TypeAlias = Literal[
    "VOICE_ISOLATION",
    "NOISE_SUPPRESSION",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEnhancementMode) -> str:
    return value


def deserialize_json(data: str) -> VoiceEnhancementMode:
    return cast(VoiceEnhancementMode, data)
