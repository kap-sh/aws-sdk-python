"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

ImageExtractionCategoryType: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "TEXT_DETECTION",
    "LOGOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> ImageExtractionCategoryType:
    return cast(ImageExtractionCategoryType, data)
