"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: TaskExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskExecutionStatus:
    return cast(TaskExecutionStatus, data)
