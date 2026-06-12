"""Generated from Smithy shape ``com.amazonaws.firehose#ParquetWriterVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ParquetWriterVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1",
        "V2",
    )
)


def serialize_aws_json_1_1(value: ParquetWriterVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParquetWriterVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ParquetWriterVersion value: {data!r}")
    return cast(ParquetWriterVersion, data)
