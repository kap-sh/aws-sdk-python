"""Generated from Smithy shape ``com.amazonaws.iot#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "MQTT",
    "HTTP",
]


# --- restJson1 ser/de ---
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
