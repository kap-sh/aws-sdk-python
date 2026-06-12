"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacCodecProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the AAC profile. For the widest player compatibility and where higher bitrates are acceptable: Keep the default profile, LC (AAC-LC) For improved audio performance at lower bitrates: Choose HEV1 or HEV2. HEV1 (AAC-HE v1) adds spectral band replication to improve speech audio at low bitrates. HEV2 (AAC-HE v2) adds parametric stereo, which optimizes for encoding stereo audio at very low bitrates. For improved audio quality at lower bitrates, adaptive audio bitrate switching, and loudness control: Choose XHE."""
AacCodecProfile: TypeAlias = Literal[
    "LC",
    "HEV1",
    "HEV2",
    "XHE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LC",
        "HEV1",
        "HEV2",
        "XHE",
    )
)


def serialize_json(value: AacCodecProfile) -> str:
    return value


def deserialize_json(data: str) -> AacCodecProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacCodecProfile value: {data!r}")
    return cast(AacCodecProfile, data)
