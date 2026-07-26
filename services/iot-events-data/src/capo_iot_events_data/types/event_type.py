"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal["STATE_CHANGE",]


# --- restJson1 ser/de ---
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
