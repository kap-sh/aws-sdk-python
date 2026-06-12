"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunSortColumnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TaskRunSortColumnType: TypeAlias = Literal[
    "TASK_RUN_TYPE",
    "STATUS",
    "STARTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TASK_RUN_TYPE",
        "STATUS",
        "STARTED",
    )
)


def serialize_aws_json_1_1(value: TaskRunSortColumnType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskRunSortColumnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskRunSortColumnType value: {data!r}")
    return cast(TaskRunSortColumnType, data)
