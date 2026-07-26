"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoExtractionCategoryType``."""

from typing import Literal, TypeAlias, cast

VideoExtractionCategoryType: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "TEXT_DETECTION",
    "TRANSCRIPT",
    "LOGOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionCategoryType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionCategoryType:
    return cast(VideoExtractionCategoryType, data)
