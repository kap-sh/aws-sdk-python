"""Generated from Smithy shape ``com.amazonaws.firehose#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

CompressionFormat: TypeAlias = Literal[
    "UNCOMPRESSED",
    "GZIP",
    "ZIP",
    "Snappy",
    "HADOOP_SNAPPY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionFormat:
    return cast(CompressionFormat, data)
