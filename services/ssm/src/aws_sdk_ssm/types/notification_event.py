"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

NotificationEvent: TypeAlias = Literal[
    "All",
    "InProgress",
    "Success",
    "TimedOut",
    "Cancelled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "InProgress",
        "Success",
        "TimedOut",
        "Cancelled",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: NotificationEvent) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationEvent value: {data!r}")
    return cast(NotificationEvent, data)
