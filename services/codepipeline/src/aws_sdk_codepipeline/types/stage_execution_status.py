"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

StageExecutionStatus: TypeAlias = Literal[
    "Cancelled",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
    "Succeeded",
    "Skipped",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cancelled",
        "InProgress",
        "Failed",
        "Stopped",
        "Stopping",
        "Succeeded",
        "Skipped",
    )
)


def serialize_aws_json_1_1(value: StageExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StageExecutionStatus value: {data!r}")
    return cast(StageExecutionStatus, data)
