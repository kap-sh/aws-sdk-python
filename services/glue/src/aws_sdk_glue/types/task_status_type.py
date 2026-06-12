"""Generated from Smithy shape ``com.amazonaws.glue#TaskStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "SUCCEEDED",
        "FAILED",
        "TIMEOUT",
    )
)


def serialize_aws_json_1_1(value: TaskStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatusType value: {data!r}")
    return cast(TaskStatusType, data)
