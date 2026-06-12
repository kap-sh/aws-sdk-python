"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationPartnerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

EventNotificationPartnerType: TypeAlias = Literal["Sidewalk",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Sidewalk",))


def serialize_json(value: EventNotificationPartnerType) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationPartnerType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EventNotificationPartnerType value: {data!r}"
        )
    return cast(EventNotificationPartnerType, data)
