"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

EventNotificationResourceType: TypeAlias = Literal[
    "SidewalkAccount",
    "WirelessDevice",
    "WirelessGateway",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SidewalkAccount",
        "WirelessDevice",
        "WirelessGateway",
    )
)


def serialize_json(value: EventNotificationResourceType) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventNotificationResourceType value: {data!r}"
        )
    return cast(EventNotificationResourceType, data)
