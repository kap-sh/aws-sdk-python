"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#KeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb_streams.errors import DeserializationError

KeyType: TypeAlias = Literal[
    "HASH",
    "RANGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HASH",
        "RANGE",
    )
)


def serialize_aws_json_1_0(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {data!r}")
    return cast(KeyType, data)
