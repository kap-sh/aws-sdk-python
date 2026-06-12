"""Generated from Smithy shape ``com.amazonaws.datasync#TaskQueueing``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TaskQueueing: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: TaskQueueing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskQueueing:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskQueueing value: {data!r}")
    return cast(TaskQueueing, data)
