"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "STARTED",
        "STOPPING",
        "STOPPED",
        "NOT_RESPONDING",
        "NOT_COMPATIBLE",
        "RUNNING",
        "IDLE",
    )
)


def serialize_json(value: WorkerStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkerStatus value: {data!r}")
    return cast(WorkerStatus, data)
