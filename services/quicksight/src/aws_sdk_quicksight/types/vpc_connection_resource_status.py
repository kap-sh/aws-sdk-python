"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnectionResourceStatus``."""

from typing import Literal, TypeAlias, cast

VPCConnectionResourceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "CREATION_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_FAILED",
    "DELETION_IN_PROGRESS",
    "DELETION_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: VPCConnectionResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> VPCConnectionResourceStatus:
    return cast(VPCConnectionResourceStatus, data)
