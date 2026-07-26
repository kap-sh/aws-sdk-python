"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionType``."""

from typing import Literal, TypeAlias, cast

AudioExtractionType: TypeAlias = Literal[
    "TRANSCRIPT",
    "SUMMARY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionType) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionType:
    return cast(AudioExtractionType, data)
