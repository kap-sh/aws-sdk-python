"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb_streams.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "INSERT",
    "MODIFY",
    "REMOVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSERT",
        "MODIFY",
        "REMOVE",
    )
)


def serialize_aws_json_1_0(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {data!r}")
    return cast(OperationType, data)
