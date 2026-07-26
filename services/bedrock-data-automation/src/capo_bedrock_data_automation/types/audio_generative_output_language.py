"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioGenerativeOutputLanguage``."""

from typing import Literal, TypeAlias, cast

"""Configuration for Audio output language"""
AudioGenerativeOutputLanguage: TypeAlias = Literal[
    "DEFAULT",
    "EN",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioGenerativeOutputLanguage) -> str:
    return value


def deserialize_json(data: str) -> AudioGenerativeOutputLanguage:
    return cast(AudioGenerativeOutputLanguage, data)
