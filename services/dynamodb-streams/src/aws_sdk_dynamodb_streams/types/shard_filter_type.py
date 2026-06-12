"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#ShardFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb_streams.errors import DeserializationError

ShardFilterType: TypeAlias = Literal["CHILD_SHARDS",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CHILD_SHARDS",))


def serialize_aws_json_1_0(value: ShardFilterType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShardFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShardFilterType value: {data!r}")
    return cast(ShardFilterType, data)
