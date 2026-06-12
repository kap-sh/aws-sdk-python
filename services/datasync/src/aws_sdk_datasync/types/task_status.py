"""Generated from Smithy shape ``com.amazonaws.datasync#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TaskStatus: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "QUEUED",
    "RUNNING",
    "UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "QUEUED",
        "RUNNING",
        "UNAVAILABLE",
    )
)


def serialize_aws_json_1_1(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
