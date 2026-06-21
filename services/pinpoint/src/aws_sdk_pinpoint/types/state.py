"""Generated from Smithy shape ``com.amazonaws.pinpoint#State``."""

from typing import Literal, TypeAlias, cast

State: TypeAlias = Literal[
    "DRAFT",
    "ACTIVE",
    "COMPLETED",
    "CANCELLED",
    "CLOSED",
    "PAUSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: State) -> str:
    return value


def deserialize_json(data: str) -> State:
    return cast(State, data)
