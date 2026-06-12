"""Generated from Smithy shape ``com.amazonaws.databrew#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "GZIP",
        "LZ4",
        "SNAPPY",
        "BZIP2",
        "DEFLATE",
        "LZO",
        "BROTLI",
        "ZSTD",
        "ZLIB",
    )
)


def serialize_json(value: CompressionFormat) -> str:
    return value


def deserialize_json(data: str) -> CompressionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionFormat value: {data!r}")
    return cast(CompressionFormat, data)
