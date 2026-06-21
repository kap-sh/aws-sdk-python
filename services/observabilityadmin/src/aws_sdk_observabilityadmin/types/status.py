"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "NOT_STARTED",
    "STARTING",
    "FAILED_START",
    "RUNNING",
    "STOPPING",
    "FAILED_STOP",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
