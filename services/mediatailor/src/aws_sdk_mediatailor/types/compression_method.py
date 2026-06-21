"""Generated from Smithy shape ``com.amazonaws.mediatailor#CompressionMethod``."""

from typing import Literal, TypeAlias, cast

CompressionMethod: TypeAlias = Literal[
    "NONE",
    "GZIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompressionMethod) -> str:
    return value


def deserialize_json(data: str) -> CompressionMethod:
    return cast(CompressionMethod, data)
