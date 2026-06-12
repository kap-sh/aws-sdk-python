"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TaskExecutionStatus: TypeAlias = Literal[
    "QUEUED",
    "CANCELLING",
    "LAUNCHING",
    "PREPARING",
    "TRANSFERRING",
    "VERIFYING",
    "SUCCESS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "CANCELLING",
        "LAUNCHING",
        "PREPARING",
        "TRANSFERRING",
        "VERIFYING",
        "SUCCESS",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: TaskExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskExecutionStatus value: {data!r}")
    return cast(TaskExecutionStatus, data)
