"""Generated from Smithy shape ``com.amazonaws.glue#ParquetCompressionType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: ParquetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetCompressionType:
    return cast(ParquetCompressionType, data)
