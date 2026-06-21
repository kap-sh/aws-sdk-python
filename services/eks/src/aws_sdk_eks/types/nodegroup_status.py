"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupStatus``."""

from typing import Literal, TypeAlias, cast

NodegroupStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
    "DEGRADED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupStatus) -> str:
    return value


def deserialize_json(data: str) -> NodegroupStatus:
    return cast(NodegroupStatus, data)
