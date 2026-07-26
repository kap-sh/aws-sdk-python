"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ColorMetadata``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Color Metadata"""
Mpeg2ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ColorMetadata:
    return cast(Mpeg2ColorMetadata, data)
