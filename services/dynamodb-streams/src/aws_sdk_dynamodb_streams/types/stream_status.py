"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#StreamStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb_streams.errors import DeserializationError

StreamStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: StreamStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StreamStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StreamStatus value: {data!r}")
    return cast(StreamStatus, data)
