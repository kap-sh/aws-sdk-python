"""Generated from Smithy shape ``com.amazonaws.datazone#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "DELETING",
        "DELETE_FAILED",
        "READY",
        "UPDATING",
        "UPDATE_FAILED",
        "DELETED",
    )
)


def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
