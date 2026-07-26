"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3CodingMode``."""

from typing import Literal, TypeAlias, cast

"""Dolby Digital Plus coding mode. Determines number of channels."""
Eac3CodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
    "CODING_MODE_3_2",
    "CODING_MODE_AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3CodingMode:
    return cast(Eac3CodingMode, data)
