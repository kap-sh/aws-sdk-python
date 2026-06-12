"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

EventType: TypeAlias = Literal["STATE_CHANGE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STATE_CHANGE",))


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
