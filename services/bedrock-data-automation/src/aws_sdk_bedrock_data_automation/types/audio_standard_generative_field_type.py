"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

AudioStandardGenerativeFieldType: TypeAlias = Literal[
    "AUDIO_SUMMARY",
    "IAB",
    "TOPIC_SUMMARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO_SUMMARY",
        "IAB",
        "TOPIC_SUMMARY",
    )
)


def serialize_json(value: AudioStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> AudioStandardGenerativeFieldType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioStandardGenerativeFieldType value: {data!r}"
        )
    return cast(AudioStandardGenerativeFieldType, data)
