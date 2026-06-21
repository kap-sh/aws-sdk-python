"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventStreamState``."""

from typing import Literal, TypeAlias, cast

EventStreamState: TypeAlias = Literal[
    "RUNNING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventStreamState) -> str:
    return value


def deserialize_json(data: str) -> EventStreamState:
    return cast(EventStreamState, data)
