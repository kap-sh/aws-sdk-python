"""Generated from Smithy shape ``com.amazonaws.firehose#CompressionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

CompressionFormat: TypeAlias = Literal[
    "UNCOMPRESSED",
    "GZIP",
    "ZIP",
    "Snappy",
    "HADOOP_SNAPPY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNCOMPRESSED",
        "GZIP",
        "ZIP",
        "Snappy",
        "HADOOP_SNAPPY",
    )
)


def serialize_aws_json_1_1(value: CompressionFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompressionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CompressionFormat value: {data!r}")
    return cast(CompressionFormat, data)
