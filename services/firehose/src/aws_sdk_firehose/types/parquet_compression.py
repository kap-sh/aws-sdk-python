"""Generated from Smithy shape ``com.amazonaws.firehose#ParquetCompression``."""

from typing import Literal, TypeAlias, cast

ParquetCompression: TypeAlias = Literal[
    "UNCOMPRESSED",
    "GZIP",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParquetCompression) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetCompression:
    return cast(ParquetCompression, data)
