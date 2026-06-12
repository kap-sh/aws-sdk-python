"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsOutputSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Indicates whether the .m3u8 manifest file should be generated for this HLS output group."""
HlsOutputSelection: TypeAlias = Literal[
    "MANIFESTS_AND_SEGMENTS",
    "SEGMENTS_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANIFESTS_AND_SEGMENTS",
        "SEGMENTS_ONLY",
    )
)


def serialize_json(value: HlsOutputSelection) -> str:
    return value


def deserialize_json(data: str) -> HlsOutputSelection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsOutputSelection value: {data!r}")
    return cast(HlsOutputSelection, data)
