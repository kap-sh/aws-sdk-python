"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "DELETE_FAILED",
        "DEGRADED",
    )
)


def serialize_json(value: NodegroupStatus) -> str:
    return value


def deserialize_json(data: str) -> NodegroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodegroupStatus value: {data!r}")
    return cast(NodegroupStatus, data)
