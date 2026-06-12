"""Generated from Smithy shape ``com.amazonaws.iot#ApplicationProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ApplicationProtocol: TypeAlias = Literal[
    "SECURE_MQTT",
    "MQTT_WSS",
    "HTTPS",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SECURE_MQTT",
        "MQTT_WSS",
        "HTTPS",
        "DEFAULT",
    )
)


def serialize_json(value: ApplicationProtocol) -> str:
    return value


def deserialize_json(data: str) -> ApplicationProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationProtocol value: {data!r}")
    return cast(ApplicationProtocol, data)
