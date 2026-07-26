"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "CANCELED",
    "PENDING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "PASS_WITH_WARNINGS",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
