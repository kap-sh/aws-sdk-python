"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#AudioGenerativeOutputLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Configuration for Audio output language"""
AudioGenerativeOutputLanguage: TypeAlias = Literal[
    "DEFAULT",
    "EN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "EN",
    )
)


def serialize_json(value: AudioGenerativeOutputLanguage) -> str:
    return value


def deserialize_json(data: str) -> AudioGenerativeOutputLanguage:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioGenerativeOutputLanguage value: {data!r}"
        )
    return cast(AudioGenerativeOutputLanguage, data)
