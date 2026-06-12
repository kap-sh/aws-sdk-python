"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mwaa_serverless.errors import DeserializationError

WorkflowRunStatus: TypeAlias = Literal[
    "STARTING",
    "QUEUED",
    "RUNNING",
    "SUCCESS",
    "FAILED",
    "TIMEOUT",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "QUEUED",
        "RUNNING",
        "SUCCESS",
        "FAILED",
        "TIMEOUT",
        "STOPPING",
        "STOPPED",
    )
)


def serialize_aws_json_1_0(value: WorkflowRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkflowRunStatus value: {data!r}")
    return cast(WorkflowRunStatus, data)
