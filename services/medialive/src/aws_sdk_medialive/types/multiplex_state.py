"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexState``."""

from typing import Literal, TypeAlias, cast

"""The current state of the multiplex."""
MultiplexState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "IDLE",
    "STARTING",
    "RUNNING",
    "RECOVERING",
    "STOPPING",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexState) -> str:
    return value


def deserialize_json(data: str) -> MultiplexState:
    return cast(MultiplexState, data)
