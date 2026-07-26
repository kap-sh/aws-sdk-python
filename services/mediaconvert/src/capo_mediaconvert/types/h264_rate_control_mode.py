"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Use this setting to specify whether this output has a variable bitrate (VBR), constant bitrate (CBR) or quality-defined variable bitrate (QVBR)."""
H264RateControlMode: TypeAlias = Literal[
    "VBR",
    "CBR",
    "QVBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H264RateControlMode:
    return cast(H264RateControlMode, data)
