"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264CodecProfile``."""

from typing import Literal, TypeAlias, cast

"""H.264 Profile. High 4:2:2 and 10-bit profiles are only available with the AVC-I License."""
H264CodecProfile: TypeAlias = Literal[
    "BASELINE",
    "HIGH",
    "HIGH_10BIT",
    "HIGH_422",
    "HIGH_422_10BIT",
    "MAIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264CodecProfile) -> str:
    return value


def deserialize_json(data: str) -> H264CodecProfile:
    return cast(H264CodecProfile, data)
