"""Generated from Smithy shape ``com.amazonaws.qapps#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "WAITING",
    "COMPLETED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
