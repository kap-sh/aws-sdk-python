"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectStatus``."""

from typing import Literal, TypeAlias, cast

ProjectStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "MOVING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectStatus) -> str:
    return value


def deserialize_json(data: str) -> ProjectStatus:
    return cast(ProjectStatus, data)
