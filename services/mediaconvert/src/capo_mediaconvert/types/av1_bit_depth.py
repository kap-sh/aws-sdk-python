"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1BitDepth``."""

from typing import Literal, TypeAlias, cast

"""Specify the Bit depth. You can choose 8-bit or 10-bit."""
Av1BitDepth: TypeAlias = Literal[
    "BIT_8",
    "BIT_10",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1BitDepth) -> str:
    return value


def deserialize_json(data: str) -> Av1BitDepth:
    return cast(Av1BitDepth, data)
