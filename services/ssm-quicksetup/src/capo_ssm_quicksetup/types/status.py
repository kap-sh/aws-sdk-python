"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "INITIALIZING",
    "DEPLOYING",
    "SUCCEEDED",
    "DELETING",
    "STOPPING",
    "FAILED",
    "STOPPED",
    "DELETE_FAILED",
    "STOP_FAILED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
