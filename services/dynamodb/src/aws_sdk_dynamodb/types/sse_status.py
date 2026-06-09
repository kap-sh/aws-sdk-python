"""Generated from Smithy shape ``com.amazonaws.dynamodb#SSEStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

SSEStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: SSEStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SSEStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SSEStatus value: {data!r}")
    return cast(SSEStatus, data)
