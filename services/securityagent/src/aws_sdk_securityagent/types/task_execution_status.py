"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Execution status of a task.</p>"""
TaskExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "ABORTED",
    "COMPLETED",
    "INTERNAL_ERROR",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskExecutionStatus:
    return cast(TaskExecutionStatus, data)
