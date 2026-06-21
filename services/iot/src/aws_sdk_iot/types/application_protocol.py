"""Generated from Smithy shape ``com.amazonaws.iot#ApplicationProtocol``."""

from typing import Literal, TypeAlias, cast

ApplicationProtocol: TypeAlias = Literal[
    "SECURE_MQTT",
    "MQTT_WSS",
    "HTTPS",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationProtocol) -> str:
    return value


def deserialize_json(data: str) -> ApplicationProtocol:
    return cast(ApplicationProtocol, data)
