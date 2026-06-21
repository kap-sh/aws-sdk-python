"""Generated from Smithy shape ``com.amazonaws.medialive#HlsTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

"""Hls Timed Metadata Id3 Frame"""
HlsTimedMetadataId3Frame: TypeAlias = Literal[
    "NONE",
    "PRIV",
    "TDRL",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> HlsTimedMetadataId3Frame:
    return cast(HlsTimedMetadataId3Frame, data)
