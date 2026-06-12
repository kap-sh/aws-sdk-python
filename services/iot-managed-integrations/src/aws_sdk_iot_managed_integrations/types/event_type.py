"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
