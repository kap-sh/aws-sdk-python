"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionStatus``."""

from typing import Literal, TypeAlias, cast

VideoExtractionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionStatus:
    return cast(VideoExtractionStatus, data)
