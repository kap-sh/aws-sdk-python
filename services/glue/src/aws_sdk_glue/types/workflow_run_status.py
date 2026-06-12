"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

WorkflowRunStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "STOPPING",
    "STOPPED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "STOPPING",
        "STOPPED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: WorkflowRunStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkflowRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowRunStatus value: {data!r}")
    return cast(WorkflowRunStatus, data)
