"""Generated from Smithy shape ``com.amazonaws.health#eventTypeCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

eventTypeCategory: TypeAlias = Literal[
    "issue",
    "accountNotification",
    "scheduledChange",
    "investigation",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "issue",
        "accountNotification",
        "scheduledChange",
        "investigation",
    )
)


def serialize_aws_json_1_1(value: eventTypeCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventTypeCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown eventTypeCategory value: {data!r}")
    return cast(eventTypeCategory, data)
