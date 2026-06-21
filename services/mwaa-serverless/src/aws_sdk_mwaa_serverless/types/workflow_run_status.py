"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: WorkflowRunStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowRunStatus:
    return cast(WorkflowRunStatus, data)
