"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "CREATION_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
    "UPDATE_FAILED",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
