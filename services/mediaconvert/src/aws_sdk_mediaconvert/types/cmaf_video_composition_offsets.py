"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafVideoCompositionOffsets``."""

from typing import Literal, TypeAlias, cast

"""Specify the video sample composition time offset mode in the output fMP4 TRUN box. For wider player compatibility, set Video composition offsets to Unsigned or leave blank. The earliest presentation time may be greater than zero, and sample composition time offsets will increment using unsigned integers. For strict fMP4 video and audio timing, set Video composition offsets to Signed. The earliest presentation time will be equal to zero, and sample composition time offsets will increment using signed integers."""
CmafVideoCompositionOffsets: TypeAlias = Literal[
    "SIGNED",
    "UNSIGNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafVideoCompositionOffsets) -> str:
    return value


def deserialize_json(data: str) -> CmafVideoCompositionOffsets:
    return cast(CmafVideoCompositionOffsets, data)
