"""Generated from Smithy shape ``com.amazonaws.qbusiness#AudioExtractionStatus``."""

from typing import Literal, TypeAlias, cast

AudioExtractionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> AudioExtractionStatus:
    return cast(AudioExtractionStatus, data)
