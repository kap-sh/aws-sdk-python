"""Generated from Smithy shape ``com.amazonaws.medialive#HlsTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls Timed Metadata Id3 Frame"""
HlsTimedMetadataId3Frame: TypeAlias = Literal[
    "NONE",
    "PRIV",
    "TDRL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PRIV",
        "TDRL",
    )
)


def serialize_json(value: HlsTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> HlsTimedMetadataId3Frame:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsTimedMetadataId3Frame value: {data!r}")
    return cast(HlsTimedMetadataId3Frame, data)
