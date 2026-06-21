"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunSortColumnType``."""

from typing import Literal, TypeAlias, cast

TaskRunSortColumnType: TypeAlias = Literal[
    "TASK_RUN_TYPE",
    "STATUS",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunSortColumnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskRunSortColumnType:
    return cast(TaskRunSortColumnType, data)
