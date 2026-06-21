"""Generated from Smithy shape ``com.amazonaws.medialive#H264RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""H264 Rate Control Mode"""
H264RateControlMode: TypeAlias = Literal[
    "CBR",
    "MULTIPLEX",
    "QVBR",
    "VBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> H264RateControlMode:
    return cast(H264RateControlMode, data)
