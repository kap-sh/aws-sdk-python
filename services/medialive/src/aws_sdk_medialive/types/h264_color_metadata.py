"""Generated from Smithy shape ``com.amazonaws.medialive#H264ColorMetadata``."""

from typing import Literal, TypeAlias, cast

"""H264 Color Metadata"""
H264ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> H264ColorMetadata:
    return cast(H264ColorMetadata, data)
