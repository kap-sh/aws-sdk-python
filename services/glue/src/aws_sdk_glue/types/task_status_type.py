"""Generated from Smithy shape ``com.amazonaws.glue#TaskStatusType``."""

from typing import Literal, TypeAlias, cast

TaskStatusType: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatusType:
    return cast(TaskStatusType, data)
