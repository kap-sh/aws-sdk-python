"""Generated from Smithy shape ``com.amazonaws.detective#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "RUNNING",
    "FAILED",
    "SUCCESSFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
