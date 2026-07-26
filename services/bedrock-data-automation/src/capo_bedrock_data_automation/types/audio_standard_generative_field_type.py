"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

AudioStandardGenerativeFieldType: TypeAlias = Literal[
    "AUDIO_SUMMARY",
    "IAB",
    "TOPIC_SUMMARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> AudioStandardGenerativeFieldType:
    return cast(AudioStandardGenerativeFieldType, data)
