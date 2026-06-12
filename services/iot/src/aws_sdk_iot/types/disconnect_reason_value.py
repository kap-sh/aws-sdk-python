"""Generated from Smithy shape ``com.amazonaws.iot#DisconnectReasonValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DisconnectReasonValue: TypeAlias = Literal[
    "AUTH_ERROR",
    "CLIENT_INITIATED_DISCONNECT",
    "CLIENT_ERROR",
    "CONNECTION_LOST",
    "DUPLICATE_CLIENTID",
    "FORBIDDEN_ACCESS",
    "MQTT_KEEP_ALIVE_TIMEOUT",
    "SERVER_ERROR",
    "SERVER_INITIATED_DISCONNECT",
    "API_INITIATED_DISCONNECT",
    "THROTTLED",
    "WEBSOCKET_TTL_EXPIRATION",
    "CUSTOMAUTH_TTL_EXPIRATION",
    "UNKNOWN",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTH_ERROR",
        "CLIENT_INITIATED_DISCONNECT",
        "CLIENT_ERROR",
        "CONNECTION_LOST",
        "DUPLICATE_CLIENTID",
        "FORBIDDEN_ACCESS",
        "MQTT_KEEP_ALIVE_TIMEOUT",
        "SERVER_ERROR",
        "SERVER_INITIATED_DISCONNECT",
        "API_INITIATED_DISCONNECT",
        "THROTTLED",
        "WEBSOCKET_TTL_EXPIRATION",
        "CUSTOMAUTH_TTL_EXPIRATION",
        "UNKNOWN",
        "NONE",
    )
)


def serialize_json(value: DisconnectReasonValue) -> str:
    return value


def deserialize_json(data: str) -> DisconnectReasonValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisconnectReasonValue value: {data!r}")
    return cast(DisconnectReasonValue, data)
