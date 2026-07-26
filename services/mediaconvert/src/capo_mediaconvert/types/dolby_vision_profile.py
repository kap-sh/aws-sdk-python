"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionProfile``."""

from typing import Literal, TypeAlias, cast

"""Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata."""
DolbyVisionProfile: TypeAlias = Literal[
    "PROFILE_5",
    "PROFILE_8_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVisionProfile) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionProfile:
    return cast(DolbyVisionProfile, data)
