"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "SKIPPED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SKIPPED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETED",
        "CANCELLED",
    )
)


def serialize_json(value: WorkflowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowExecutionStatus value: {data!r}")
    return cast(WorkflowExecutionStatus, data)
