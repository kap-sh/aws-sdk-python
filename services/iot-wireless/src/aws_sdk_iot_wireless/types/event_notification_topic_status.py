"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationTopicStatus``."""

from typing import Literal, TypeAlias, cast

EventNotificationTopicStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventNotificationTopicStatus) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationTopicStatus:
    return cast(EventNotificationTopicStatus, data)
