"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NodeStatus) -> str:
    return value


def deserialize_json(data: str) -> NodeStatus:
    return cast(NodeStatus, data)
