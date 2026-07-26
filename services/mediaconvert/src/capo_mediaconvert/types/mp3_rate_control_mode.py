"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp3RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Specify whether the service encodes this MP3 audio output with a constant bitrate (CBR) or a variable bitrate (VBR)."""
Mp3RateControlMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mp3RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Mp3RateControlMode:
    return cast(Mp3RateControlMode, data)
