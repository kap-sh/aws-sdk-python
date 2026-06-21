"""Generated from Smithy shape ``com.amazonaws.medialive#CmafTimedMetadataPassthrough``."""

from typing import Literal, TypeAlias, cast

"""Cmaf Timed Metadata Passthrough"""
CmafTimedMetadataPassthrough: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafTimedMetadataPassthrough) -> str:
    return value


def deserialize_json(data: str) -> CmafTimedMetadataPassthrough:
    return cast(CmafTimedMetadataPassthrough, data)
