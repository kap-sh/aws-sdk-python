"""Generated from Smithy shape ``com.amazonaws.ebs#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "completed",
    "pending",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
