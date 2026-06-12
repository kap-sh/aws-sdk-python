"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationTopicStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

EventNotificationTopicStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: EventNotificationTopicStatus) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationTopicStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventNotificationTopicStatus value: {data!r}"
        )
    return cast(EventNotificationTopicStatus, data)
