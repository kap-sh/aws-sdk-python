"""Generated from Smithy shape ``com.amazonaws.glue#ParquetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ParquetCompressionType: TypeAlias = Literal[
    "snappy",
    "lzo",
    "gzip",
    "brotli",
    "lz4",
    "uncompressed",
    "none",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "snappy",
        "lzo",
        "gzip",
        "brotli",
        "lz4",
        "uncompressed",
        "none",
    )
)


def serialize_aws_json_1_1(value: ParquetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParquetCompressionType value: {data!r}")
    return cast(ParquetCompressionType, data)
