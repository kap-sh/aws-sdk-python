"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

ConnectionStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
    "READY",
    "UPDATING",
    "UPDATE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    return cast(ConnectionStatus, data)
