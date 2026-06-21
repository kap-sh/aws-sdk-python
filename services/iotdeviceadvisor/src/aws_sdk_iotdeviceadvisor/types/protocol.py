"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "MqttV3_1_1",
    "MqttV5",
    "MqttV3_1_1_OverWebSocket",
    "MqttV5_OverWebSocket",
]


# --- restJson1 ser/de ---
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
