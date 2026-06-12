"""Generated from Smithy shape ``com.amazonaws.firehose#ParquetCompression``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ParquetCompression: TypeAlias = Literal[
    "UNCOMPRESSED",
    "GZIP",
    "SNAPPY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNCOMPRESSED",
        "GZIP",
        "SNAPPY",
    )
)


def serialize_aws_json_1_1(value: ParquetCompression) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetCompression:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParquetCompression value: {data!r}")
    return cast(ParquetCompression, data)
