"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UPDATING",
    "UPDATE_FAILED",
    "READY",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
