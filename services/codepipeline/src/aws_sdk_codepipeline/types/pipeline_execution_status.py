"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

PipelineExecutionStatus: TypeAlias = Literal[
    "Cancelled",
    "InProgress",
    "Stopped",
    "Stopping",
    "Succeeded",
    "Superseded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cancelled",
        "InProgress",
        "Stopped",
        "Stopping",
        "Succeeded",
        "Superseded",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: PipelineExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PipelineExecutionStatus value: {data!r}")
    return cast(PipelineExecutionStatus, data)
