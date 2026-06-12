"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

VideoExtractionCategoryType: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "TEXT_DETECTION",
    "TRANSCRIPT",
    "LOGOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTENT_MODERATION",
        "TEXT_DETECTION",
        "TRANSCRIPT",
        "LOGOS",
    )
)


def serialize_json(value: VideoExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionCategoryType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VideoExtractionCategoryType value: {data!r}"
        )
    return cast(VideoExtractionCategoryType, data)
