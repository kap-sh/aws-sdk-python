"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Required when you enable Dolby Vision. Use Profile 5 to include frame-interleaved Dolby Vision metadata in your output. Your input must include Dolby Vision metadata or an HDR10 YUV color space. Use Profile 8.1 to include frame-interleaved Dolby Vision metadata and HDR10 metadata in your output. Your input must include Dolby Vision metadata."""
DolbyVisionProfile: TypeAlias = Literal[
    "PROFILE_5",
    "PROFILE_8_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE_5",
        "PROFILE_8_1",
    )
)


def serialize_json(value: DolbyVisionProfile) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DolbyVisionProfile value: {data!r}")
    return cast(DolbyVisionProfile, data)
