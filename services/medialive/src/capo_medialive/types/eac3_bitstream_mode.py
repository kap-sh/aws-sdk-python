"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Bitstream Mode"""
Eac3BitstreamMode: TypeAlias = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "VISUALLY_IMPAIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3BitstreamMode:
    return cast(Eac3BitstreamMode, data)
