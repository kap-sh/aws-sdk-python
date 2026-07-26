"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourcePosition``."""

from typing import Literal, TypeAlias, cast

EventSourcePosition: TypeAlias = Literal[
    "TRIM_HORIZON",
    "LATEST",
    "AT_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourcePosition) -> str:
    return value


def deserialize_json(data: str) -> EventSourcePosition:
    return cast(EventSourcePosition, data)
