"""Generated from Smithy shape ``com.amazonaws.connect#ExecutionRecordStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionRecordStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionRecordStatus:
    return cast(ExecutionRecordStatus, data)
