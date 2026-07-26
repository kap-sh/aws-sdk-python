"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacCodingMode``."""

from typing import Literal, TypeAlias, cast

"""The Coding mode that you specify determines the number of audio channels and the audio channel layout metadata in your AAC output. Valid coding modes depend on the Rate control mode and Profile that you select. The following list shows the number of audio channels and channel layout for each coding mode. * 1.0 Audio Description (Receiver Mix): One channel, C. Includes audio description data from your stereo input. For more information see ETSI TS 101 154 Annex E. * 1.0 Mono: One channel, C. * 2.0 Stereo: Two channels, L, R. * 5.1 Surround: Six channels, C, L, R, Ls, Rs, LFE. To follow the number of channels from your input audio, choose CODING_MODE_AUTO, and the service will automatically choose from one of the coding modes above."""
AacCodingMode: TypeAlias = Literal[
    "AD_RECEIVER_MIX",
    "CODING_MODE_1_0",
    "CODING_MODE_1_1",
    "CODING_MODE_2_0",
    "CODING_MODE_5_1",
    "CODING_MODE_AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacCodingMode) -> str:
    return value


def deserialize_json(data: str) -> AacCodingMode:
    return cast(AacCodingMode, data)
