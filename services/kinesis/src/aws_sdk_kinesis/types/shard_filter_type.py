"""Generated from Smithy shape ``com.amazonaws.kinesis#ShardFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis.errors import DeserializationError

ShardFilterType: TypeAlias = Literal[
    "AFTER_SHARD_ID",
    "AT_TRIM_HORIZON",
    "FROM_TRIM_HORIZON",
    "AT_LATEST",
    "AT_TIMESTAMP",
    "FROM_TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AFTER_SHARD_ID",
        "AT_TRIM_HORIZON",
        "FROM_TRIM_HORIZON",
        "AT_LATEST",
        "AT_TIMESTAMP",
        "FROM_TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: ShardFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShardFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShardFilterType value: {data!r}")
    return cast(ShardFilterType, data)
