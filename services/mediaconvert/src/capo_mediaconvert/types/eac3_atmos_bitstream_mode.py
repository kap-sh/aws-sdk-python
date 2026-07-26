"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosBitstreamMode``."""

from typing import Literal, TypeAlias, cast

"""Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
Eac3AtmosBitstreamMode: TypeAlias = Literal["COMPLETE_MAIN",]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosBitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosBitstreamMode:
    return cast(Eac3AtmosBitstreamMode, data)
