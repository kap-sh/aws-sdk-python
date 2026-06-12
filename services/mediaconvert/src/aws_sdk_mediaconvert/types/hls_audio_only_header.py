"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsAudioOnlyHeader``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless you are using FairPlay DRM with Verimatrix and you encounter playback issues. Keep the default value, Include, to output audio-only headers. Choose Exclude to remove the audio-only headers from your audio segments."""
HlsAudioOnlyHeader: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUDE",
        "EXCLUDE",
    )
)


def serialize_json(value: HlsAudioOnlyHeader) -> str:
    return value


def deserialize_json(data: str) -> HlsAudioOnlyHeader:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsAudioOnlyHeader value: {data!r}")
    return cast(HlsAudioOnlyHeader, data)
