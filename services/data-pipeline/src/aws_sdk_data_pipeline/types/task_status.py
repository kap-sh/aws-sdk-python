"""Generated from Smithy shape ``com.amazonaws.datapipeline#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_data_pipeline.errors import DeserializationError

TaskStatus: TypeAlias = Literal[
    "FINISHED",
    "FAILED",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINISHED",
        "FAILED",
        "FALSE",
    )
)


def serialize_aws_json_1_1(value: TaskStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
