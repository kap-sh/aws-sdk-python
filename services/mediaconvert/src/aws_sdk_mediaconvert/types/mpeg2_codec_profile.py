"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2CodecProfile``."""

from typing import Literal, TypeAlias, cast

"""Use Profile to set the MPEG-2 profile for the video output."""
Mpeg2CodecProfile: TypeAlias = Literal[
    "MAIN",
    "PROFILE_422",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2CodecProfile) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2CodecProfile:
    return cast(Mpeg2CodecProfile, data)
