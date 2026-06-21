"""Generated from Smithy shape ``com.amazonaws.medialive#UdpTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

"""Udp Timed Metadata Id3 Frame"""
UdpTimedMetadataId3Frame: TypeAlias = Literal[
    "NONE",
    "PRIV",
    "TDRL",
]


# --- restJson1 ser/de ---
def serialize_json(value: UdpTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> UdpTimedMetadataId3Frame:
    return cast(UdpTimedMetadataId3Frame, data)
