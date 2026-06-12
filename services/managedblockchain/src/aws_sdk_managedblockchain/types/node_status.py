"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_managedblockchain.errors import DeserializationError

NodeStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "UNHEALTHY",
    "CREATE_FAILED",
    "UPDATING",
    "DELETING",
    "DELETED",
    "FAILED",
    "INACCESSIBLE_ENCRYPTION_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "UNHEALTHY",
        "CREATE_FAILED",
        "UPDATING",
        "DELETING",
        "DELETED",
        "FAILED",
        "INACCESSIBLE_ENCRYPTION_KEY",
    )
)


def serialize_json(value: NodeStatus) -> str:
    return value


def deserialize_json(data: str) -> NodeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeStatus value: {data!r}")
    return cast(NodeStatus, data)
