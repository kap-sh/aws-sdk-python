"""Generated from Smithy shape ``com.amazonaws.datasync#TaskMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TaskMode: TypeAlias = Literal[
    "BASIC",
    "ENHANCED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "ENHANCED",
    )
)


def serialize_aws_json_1_1(value: TaskMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskMode value: {data!r}")
    return cast(TaskMode, data)
