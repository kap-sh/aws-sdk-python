"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2CodecProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Profile to set the MPEG-2 profile for the video output."""
Mpeg2CodecProfile: TypeAlias = Literal[
    "MAIN",
    "PROFILE_422",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAIN",
        "PROFILE_422",
    )
)


def serialize_json(value: Mpeg2CodecProfile) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2CodecProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2CodecProfile value: {data!r}")
    return cast(Mpeg2CodecProfile, data)
