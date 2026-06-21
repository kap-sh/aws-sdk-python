"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsRateMode``."""

from typing import Literal, TypeAlias, cast

"""M2ts Rate Mode"""
M2tsRateMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsRateMode) -> str:
    return value


def deserialize_json(data: str) -> M2tsRateMode:
    return cast(M2tsRateMode, data)
