"""Generated from Smithy shape ``com.amazonaws.finspace#KxClusterStatus``."""

from typing import Literal, TypeAlias, cast

KxClusterStatus: TypeAlias = Literal[
    "PENDING",
    "CREATING",
    "CREATE_FAILED",
    "RUNNING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxClusterStatus) -> str:
    return value


def deserialize_json(data: str) -> KxClusterStatus:
    return cast(KxClusterStatus, data)
