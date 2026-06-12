"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionRollbackStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

WorkflowStepExecutionRollbackStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "SKIPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "SKIPPED",
        "FAILED",
    )
)


def serialize_json(value: WorkflowStepExecutionRollbackStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepExecutionRollbackStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkflowStepExecutionRollbackStatus value: {data!r}"
        )
    return cast(WorkflowStepExecutionRollbackStatus, data)
