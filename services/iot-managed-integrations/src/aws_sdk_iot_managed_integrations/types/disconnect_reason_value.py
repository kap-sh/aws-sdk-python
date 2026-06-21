"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DisconnectReasonValue``."""

from typing import Literal, TypeAlias, cast

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
    "THROTTLED",
    "WEBSOCKET_TTL_EXPIRATION",
    "CUSTOMAUTH_TTL_EXPIRATION",
    "UNKNOWN",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectReasonValue) -> str:
    return value


def deserialize_json(data: str) -> DisconnectReasonValue:
    return cast(DisconnectReasonValue, data)
