"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac4BitstreamMode``."""

from typing import Literal, TypeAlias, cast

"""Specify the bitstream mode for the AC-4 stream that the encoder emits. For more information about the AC-4 bitstream mode, see ETSI TS 103 190. Maps to dlb_paec_ac4_bed_classifier in the encoder implementation. - COMPLETE_MAIN: Complete Main (standard mix) - EMERGENCY: Stereo Emergency content"""
Ac4BitstreamMode: TypeAlias = Literal[
    "COMPLETE_MAIN",
    "EMERGENCY",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac4BitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Ac4BitstreamMode:
    return cast(Ac4BitstreamMode, data)
