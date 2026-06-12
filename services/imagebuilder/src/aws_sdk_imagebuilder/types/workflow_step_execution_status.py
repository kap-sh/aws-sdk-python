"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowStepExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "SKIPPED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
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
        "CANCELLED",
    )
)


def serialize_json(value: WorkflowStepExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkflowStepExecutionStatus value: {data!r}"
        )
    return cast(WorkflowStepExecutionStatus, data)
