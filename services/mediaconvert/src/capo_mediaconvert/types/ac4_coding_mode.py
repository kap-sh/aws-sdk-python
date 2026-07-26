"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Ac4CodingMode``."""

from typing import Literal, TypeAlias, cast

"""Dolby AC-4 coding mode. Determines number of channels. Maps to dlb_paec_ac4_bed_channel_config in the encoder implementation. - CODING_MODE_2_0: 2.0 (stereo) - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_20 - CODING_MODE_3_2_LFE: 5.1 surround - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_51 - CODING_MODE_5_1_4: 5.1.4 immersive - maps to DLB_PAEC_AC4_BED_CHANNEL_CONFIG_514"""
Ac4CodingMode: TypeAlias = Literal[
    "CODING_MODE_2_0",
    "CODING_MODE_3_2_LFE",
    "CODING_MODE_5_1_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: Ac4CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Ac4CodingMode:
    return cast(Ac4CodingMode, data)
