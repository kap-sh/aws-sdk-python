"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionState``."""

from typing import Literal, TypeAlias, cast

ExecutionState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionState) -> str:
    return value


def deserialize_json(data: str) -> ExecutionState:
    return cast(ExecutionState, data)
