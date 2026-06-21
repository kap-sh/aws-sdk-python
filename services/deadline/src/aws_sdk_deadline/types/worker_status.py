"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerStatus``."""

from typing import Literal, TypeAlias, cast

WorkerStatus: TypeAlias = Literal[
    "CREATED",
    "STARTED",
    "STOPPING",
    "STOPPED",
    "NOT_RESPONDING",
    "NOT_COMPATIBLE",
    "RUNNING",
    "IDLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkerStatus:
    return cast(WorkerStatus, data)
