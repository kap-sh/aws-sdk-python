"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2DisplayRatio``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Display Ratio"""
Mpeg2DisplayRatio: TypeAlias = Literal[
    "DISPLAYRATIO16X9",
    "DISPLAYRATIO4X3",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2DisplayRatio) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2DisplayRatio:
    return cast(Mpeg2DisplayRatio, data)
