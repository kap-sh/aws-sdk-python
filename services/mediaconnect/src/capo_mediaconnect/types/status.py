"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "STANDBY",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "STARTING",
    "STOPPING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
