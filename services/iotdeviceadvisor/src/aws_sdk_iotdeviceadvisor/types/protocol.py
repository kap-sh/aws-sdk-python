"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#Protocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

Protocol: TypeAlias = Literal[
    "MqttV3_1_1",
    "MqttV5",
    "MqttV3_1_1_OverWebSocket",
    "MqttV5_OverWebSocket",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MqttV3_1_1",
        "MqttV5",
        "MqttV3_1_1_OverWebSocket",
        "MqttV5_OverWebSocket",
    )
)


def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Protocol value: {data!r}")
    return cast(Protocol, data)
