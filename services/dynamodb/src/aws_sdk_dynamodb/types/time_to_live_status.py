"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

TimeToLiveStatus: TypeAlias = Literal[
    "ENABLING",
    "DISABLING",
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "DISABLING",
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: TimeToLiveStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TimeToLiveStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeToLiveStatus value: {data!r}")
    return cast(TimeToLiveStatus, data)
