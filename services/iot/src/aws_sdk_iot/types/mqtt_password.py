"""Generated from Smithy shape ``com.amazonaws.iot#MqttPassword``."""

import base64
from typing import TypeAlias

MqttPassword: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: MqttPassword) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> MqttPassword:
    return base64.b64decode(data)
