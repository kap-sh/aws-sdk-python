"""Generated from Smithy shape ``com.amazonaws.iot#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Cancelled",
    "Cancelling",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
