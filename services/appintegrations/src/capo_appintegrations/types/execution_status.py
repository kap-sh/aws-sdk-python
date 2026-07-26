"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
