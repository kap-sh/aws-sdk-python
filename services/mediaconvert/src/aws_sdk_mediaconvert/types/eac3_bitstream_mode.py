"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3BitstreamMode``."""

from typing import Literal, TypeAlias, cast

"""Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
Eac3BitstreamMode: TypeAlias = Literal[
    "COMPLETE_MAIN",
    "COMMENTARY",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "VISUALLY_IMPAIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3BitstreamMode:
    return cast(Eac3BitstreamMode, data)
