"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VideoExtractionType: TypeAlias = Literal[
    "AUDIO_TRANSCRIPTION_ONLY",
    "VISUAL_CONTENT_AND_AUDIO_TRANSCRIPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUDIO_TRANSCRIPTION_ONLY",
        "VISUAL_CONTENT_AND_AUDIO_TRANSCRIPTION",
    )
)


def serialize_json(value: VideoExtractionType) -> str:
    return value


def deserialize_json(data: str) -> VideoExtractionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoExtractionType value: {data!r}")
    return cast(VideoExtractionType, data)
