"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "InProgress",
    "Successful",
    "Error",
    "CancelStarted",
    "Canceled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
