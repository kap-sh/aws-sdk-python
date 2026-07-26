"""Generated from Smithy shape ``com.amazonaws.databrew#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

CompressionFormat: TypeAlias = Literal[
    "GZIP",
    "LZ4",
    "SNAPPY",
    "BZIP2",
    "DEFLATE",
    "LZO",
    "BROTLI",
    "ZSTD",
    "ZLIB",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompressionFormat) -> str:
    return value


def deserialize_json(data: str) -> CompressionFormat:
    return cast(CompressionFormat, data)
