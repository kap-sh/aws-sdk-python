"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowRunStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "STOPPING",
    "STOPPED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowRunStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkflowRunStatus:
    return cast(WorkflowRunStatus, data)
