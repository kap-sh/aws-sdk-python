"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#VoiceEngine``."""

from typing import Literal, TypeAlias, cast

VoiceEngine: TypeAlias = Literal[
    "standard",
    "neural",
    "long-form",
    "generative",
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceEngine) -> str:
    return value


def deserialize_json(data: str) -> VoiceEngine:
    return cast(VoiceEngine, data)
