"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Execution status of a task.</p>"""
TaskExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "ABORTED",
    "COMPLETED",
    "INTERNAL_ERROR",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "ABORTED",
        "COMPLETED",
        "INTERNAL_ERROR",
        "FAILED",
    )
)


def serialize_json(value: TaskExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskExecutionStatus value: {data!r}")
    return cast(TaskExecutionStatus, data)
