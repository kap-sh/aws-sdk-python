"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Use Rate control mode to specify whether the bitrate is variable (vbr) or constant (cbr)."""
Mpeg2RateControlMode: TypeAlias = Literal[
    "VBR",
    "CBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2RateControlMode:
    return cast(Mpeg2RateControlMode, data)
