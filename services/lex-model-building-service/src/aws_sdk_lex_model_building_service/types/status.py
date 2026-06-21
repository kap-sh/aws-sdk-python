"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Status``."""

from typing import Literal, TypeAlias, cast

Status: TypeAlias = Literal[
    "BUILDING",
    "READY",
    "READY_BASIC_TESTING",
    "FAILED",
    "NOT_BUILT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Status) -> str:
    return value


def deserialize_json(data: str) -> Status:
    return cast(Status, data)
