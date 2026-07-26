"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2CodecLevel``."""

from typing import Literal, TypeAlias, cast

"""Use Level to set the MPEG-2 level for the video output."""
Mpeg2CodecLevel: TypeAlias = Literal[
    "AUTO",
    "LOW",
    "MAIN",
    "HIGH1440",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2CodecLevel) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2CodecLevel:
    return cast(Mpeg2CodecLevel, data)
