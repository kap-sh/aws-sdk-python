"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Gop Size Units"""
Mpeg2GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2GopSizeUnits:
    return cast(Mpeg2GopSizeUnits, data)
