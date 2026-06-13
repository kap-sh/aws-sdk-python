"""Generated from Smithy shape ``com.amazonaws.keyspacesstreams#ShardIteratorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_keyspacesstreams.errors import DeserializationError

ShardIteratorType: TypeAlias = Literal[
    "TRIM_HORIZON",
    "LATEST",
    "AT_SEQUENCE_NUMBER",
    "AFTER_SEQUENCE_NUMBER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRIM_HORIZON",
        "LATEST",
        "AT_SEQUENCE_NUMBER",
        "AFTER_SEQUENCE_NUMBER",
    )
)


def serialize_aws_json_1_0(value: ShardIteratorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShardIteratorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShardIteratorType value: {data!r}")
    return cast(ShardIteratorType, data)
