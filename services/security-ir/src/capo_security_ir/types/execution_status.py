"""Generated from Smithy shape ``com.amazonaws.securityir#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Waiting",
    "Completed",
    "Failed",
    "Cancelled",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
