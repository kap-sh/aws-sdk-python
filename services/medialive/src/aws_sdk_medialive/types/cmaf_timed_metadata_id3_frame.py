"""Generated from Smithy shape ``com.amazonaws.medialive#CmafTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Cmaf Timed Metadata Id3 Frame"""
CmafTimedMetadataId3Frame: TypeAlias = Literal[
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


def serialize_json(value: CmafTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> CmafTimedMetadataId3Frame:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafTimedMetadataId3Frame value: {data!r}")
    return cast(CmafTimedMetadataId3Frame, data)
