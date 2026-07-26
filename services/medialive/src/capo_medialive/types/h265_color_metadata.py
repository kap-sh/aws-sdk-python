"""Generated from Smithy shape ``com.amazonaws.medialive#H265ColorMetadata``."""

from typing import Literal, TypeAlias, cast

"""H265 Color Metadata"""
H265ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> H265ColorMetadata:
    return cast(H265ColorMetadata, data)
