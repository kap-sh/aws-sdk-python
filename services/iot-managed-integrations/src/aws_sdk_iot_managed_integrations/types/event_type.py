"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal[
    "DEVICE_COMMAND",
    "DEVICE_COMMAND_REQUEST",
    "DEVICE_DISCOVERY_STATUS",
    "DEVICE_EVENT",
    "DEVICE_LIFE_CYCLE",
    "DEVICE_STATE",
    "DEVICE_OTA",
    "DEVICE_WSS",
    "CONNECTOR_ASSOCIATION",
    "ACCOUNT_ASSOCIATION",
    "CONNECTOR_ERROR_REPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
