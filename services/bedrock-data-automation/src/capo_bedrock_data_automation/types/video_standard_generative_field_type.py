"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VideoStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

VideoStandardGenerativeFieldType: TypeAlias = Literal[
    "VIDEO_SUMMARY",
    "IAB",
    "CHAPTER_SUMMARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> VideoStandardGenerativeFieldType:
    return cast(VideoStandardGenerativeFieldType, data)
