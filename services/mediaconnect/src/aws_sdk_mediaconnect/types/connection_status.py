"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)
