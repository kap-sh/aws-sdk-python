"""Generated from Smithy shape ``com.amazonaws.dynamodb#DestinationStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

DestinationStatus: TypeAlias = Literal[
    "ENABLING",
    "ACTIVE",
    "DISABLING",
    "DISABLED",
    "ENABLE_FAILED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ACTIVE",
        "DISABLING",
        "DISABLED",
        "ENABLE_FAILED",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: DestinationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DestinationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationStatus value: {data!r}")
    return cast(DestinationStatus, data)
