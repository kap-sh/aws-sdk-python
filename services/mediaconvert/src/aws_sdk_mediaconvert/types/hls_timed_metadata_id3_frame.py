"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsTimedMetadataId3Frame``."""

from typing import Literal, TypeAlias, cast

"""Specify the type of the ID3 frame to use for ID3 timestamps in your output. To include ID3 timestamps: Specify PRIV or TDRL and set ID3 metadata to Passthrough. To exclude ID3 timestamps: Set ID3 timestamp frame type to None."""
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
