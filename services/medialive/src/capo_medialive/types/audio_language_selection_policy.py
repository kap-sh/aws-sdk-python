"""Generated from Smithy shape ``com.amazonaws.medialive#AudioLanguageSelectionPolicy``."""

from typing import Literal, TypeAlias, cast

"""Audio Language Selection Policy"""
AudioLanguageSelectionPolicy: TypeAlias = Literal[
    "LOOSE",
    "STRICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioLanguageSelectionPolicy) -> str:
    return value


def deserialize_json(data: str) -> AudioLanguageSelectionPolicy:
    return cast(AudioLanguageSelectionPolicy, data)
