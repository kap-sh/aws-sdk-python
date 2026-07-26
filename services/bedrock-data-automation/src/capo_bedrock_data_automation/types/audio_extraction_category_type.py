"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

AudioExtractionCategoryType: TypeAlias = Literal[
    "AUDIO_CONTENT_MODERATION",
    "TRANSCRIPT",
    "TOPIC_CONTENT_MODERATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionCategoryType:
    return cast(AudioExtractionCategoryType, data)
