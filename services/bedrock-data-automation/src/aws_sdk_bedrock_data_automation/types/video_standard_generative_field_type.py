"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

VideoStandardGenerativeFieldType: TypeAlias = Literal[
    "VIDEO_SUMMARY",
    "IAB",
    "CHAPTER_SUMMARY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIDEO_SUMMARY",
        "IAB",
        "CHAPTER_SUMMARY",
    )
)


def serialize_json(value: VideoStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> VideoStandardGenerativeFieldType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VideoStandardGenerativeFieldType value: {data!r}"
        )
    return cast(VideoStandardGenerativeFieldType, data)
