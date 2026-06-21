"""Generated from Smithy shape ``com.amazonaws.connect#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "COMPLETE",
    "IN_PROGRESS",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
