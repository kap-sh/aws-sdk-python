"""Generated from Smithy shape ``com.amazonaws.iotwireless#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "Connected",
    "Disconnected",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)
