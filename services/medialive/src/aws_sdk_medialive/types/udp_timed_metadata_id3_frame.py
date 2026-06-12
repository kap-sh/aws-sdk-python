"""Generated from Smithy shape ``com.amazonaws.medialive#UdpTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Udp Timed Metadata Id3 Frame"""
UdpTimedMetadataId3Frame: TypeAlias = Literal[
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


def serialize_json(value: UdpTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> UdpTimedMetadataId3Frame:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UdpTimedMetadataId3Frame value: {data!r}")
    return cast(UdpTimedMetadataId3Frame, data)
