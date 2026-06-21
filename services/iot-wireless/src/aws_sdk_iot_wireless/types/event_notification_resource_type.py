"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationResourceType``."""

from typing import Literal, TypeAlias, cast

EventNotificationResourceType: TypeAlias = Literal[
    "SidewalkAccount",
    "WirelessDevice",
    "WirelessGateway",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventNotificationResourceType) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationResourceType:
    return cast(EventNotificationResourceType, data)
