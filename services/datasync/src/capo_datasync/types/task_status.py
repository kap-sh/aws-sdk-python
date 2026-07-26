"""Generated from Smithy shape ``com.amazonaws.datasync#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "QUEUED",
    "RUNNING",
    "UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
