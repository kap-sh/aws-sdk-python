"""Generated from Smithy shape ``com.amazonaws.medialive#Av1GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""Av1 Gop Size Units"""
Av1GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> Av1GopSizeUnits:
    return cast(Av1GopSizeUnits, data)
