"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

ImageExtractionCategoryType: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "TEXT_DETECTION",
    "LOGOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTENT_MODERATION",
        "TEXT_DETECTION",
        "LOGOS",
    )
)


def serialize_json(value: ImageExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> ImageExtractionCategoryType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageExtractionCategoryType value: {data!r}"
        )
    return cast(ImageExtractionCategoryType, data)
