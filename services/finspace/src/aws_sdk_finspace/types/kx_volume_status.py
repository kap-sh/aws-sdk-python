"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolumeStatus``."""

from typing import Literal, TypeAlias, cast

KxVolumeStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "UPDATING",
    "UPDATED",
    "UPDATE_FAILED",
    "DELETING",
    "DELETED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KxVolumeStatus) -> str:
    return value


def deserialize_json(data: str) -> KxVolumeStatus:
    return cast(KxVolumeStatus, data)
