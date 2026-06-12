"""Generated from Smithy shape ``com.amazonaws.kinesis#ShardIteratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

ShardIteratorType: TypeAlias = Literal[
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
    "TRIM_HORIZON",
    "LATEST",
    "AT_TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AT_SEQUENCE_NUMBER",
        "AFTER_SEQUENCE_NUMBER",
        "TRIM_HORIZON",
        "LATEST",
        "AT_TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: ShardIteratorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShardIteratorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShardIteratorType value: {data!r}")
    return cast(ShardIteratorType, data)
