"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionType``."""

from typing import Literal, TypeAlias, cast

ConnectionType: TypeAlias = Literal[
    "BGP",
    "IPSEC",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionType:
    return cast(ConnectionType, data)
