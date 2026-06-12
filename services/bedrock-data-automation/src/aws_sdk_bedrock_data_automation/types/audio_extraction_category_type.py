"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

AudioExtractionCategoryType: TypeAlias = Literal[
    "AUDIO_CONTENT_MODERATION",
    "TRANSCRIPT",
    "TOPIC_CONTENT_MODERATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO_CONTENT_MODERATION",
        "TRANSCRIPT",
        "TOPIC_CONTENT_MODERATION",
    )
)


def serialize_json(value: AudioExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionCategoryType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioExtractionCategoryType value: {data!r}"
        )
    return cast(AudioExtractionCategoryType, data)
