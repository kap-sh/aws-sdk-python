"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionType``."""

from typing import Literal, TypeAlias, cast

VideoExtractionType: TypeAlias = Literal[
    "AUDIO_TRANSCRIPTION_ONLY",
    "VISUAL_CONTENT_AND_AUDIO_TRANSCRIPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionType:
    return cast(VideoExtractionType, data)
