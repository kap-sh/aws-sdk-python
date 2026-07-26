"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TraversalDirection``."""

from typing import Literal, TypeAlias, cast

TraversalDirection: TypeAlias = Literal[
    "PARENT",
    "CHILD",
]


# --- restJson1 ser/de ---
def serialize_json(value: TraversalDirection) -> str:
    return value


def deserialize_json(data: str) -> TraversalDirection:
    return cast(TraversalDirection, data)
