"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionState``."""

from typing import Literal, TypeAlias, cast

ConnectionState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionState) -> str:
    return value


def deserialize_json(data: str) -> ConnectionState:
    return cast(ConnectionState, data)
