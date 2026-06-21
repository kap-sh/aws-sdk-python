"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventNotificationPartnerType``."""

from typing import Literal, TypeAlias, cast

EventNotificationPartnerType: TypeAlias = Literal["Sidewalk",]


# --- restJson1 ser/de ---
def serialize_json(value: EventNotificationPartnerType) -> str:
    return value


def deserialize_json(data: str) -> EventNotificationPartnerType:
    return cast(EventNotificationPartnerType, data)
