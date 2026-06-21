"""Generated from Smithy shape ``com.amazonaws.qbusiness#VideoExtractionType``."""

from typing import Literal, TypeAlias, cast

VideoExtractionType: TypeAlias = Literal[
    "TRANSCRIPT",
    "SUMMARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionType:
    return cast(VideoExtractionType, data)
