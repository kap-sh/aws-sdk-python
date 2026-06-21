"""Generated from Smithy shape ``com.amazonaws.medialive#Av1BitDepth``."""

from typing import Literal, TypeAlias, cast

"""Av1 Bit Depth"""
Av1BitDepth: TypeAlias = Literal[
    "DEPTH_10",
    "DEPTH_8",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1BitDepth) -> str:
    return value


def deserialize_json(data: str) -> Av1BitDepth:
    return cast(Av1BitDepth, data)
