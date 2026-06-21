"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

EnvironmentStatus: TypeAlias = Literal[
    "ACTIVE",
    "CREATING",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
    "VALIDATION_FAILED",
    "SUSPENDED",
    "DISABLED",
    "EXPIRED",
    "DELETED",
    "INACCESSIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentStatus) -> str:
    return value


def deserialize_json(data: str) -> EnvironmentStatus:
    return cast(EnvironmentStatus, data)
