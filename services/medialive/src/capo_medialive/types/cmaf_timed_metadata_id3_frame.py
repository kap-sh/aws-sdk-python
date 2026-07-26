"""Generated from Smithy shape ``com.amazonaws.medialive#CmafTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

"""Cmaf Timed Metadata Id3 Frame"""
CmafTimedMetadataId3Frame: TypeAlias = Literal[
    "NONE",
    "PRIV",
    "TDRL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafTimedMetadataId3Frame) -> str:
    return value


def deserialize_json(data: str) -> CmafTimedMetadataId3Frame:
    return cast(CmafTimedMetadataId3Frame, data)
