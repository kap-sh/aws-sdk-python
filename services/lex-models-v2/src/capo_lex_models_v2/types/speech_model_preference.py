"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechModelPreference``."""

from typing import Literal, TypeAlias, cast

SpeechModelPreference: TypeAlias = Literal[
    "Standard",
    "Neural",
    "Deepgram",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpeechModelPreference) -> str:
    return value


def deserialize_json(data: str) -> SpeechModelPreference:
    return cast(SpeechModelPreference, data)
