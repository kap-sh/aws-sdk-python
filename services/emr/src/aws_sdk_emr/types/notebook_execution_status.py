"""Generated from Smithy shape ``com.amazonaws.emr#NotebookExecutionStatus``."""

from typing import Literal, TypeAlias, cast

NotebookExecutionStatus: TypeAlias = Literal[
    "START_PENDING",
    "STARTING",
    "RUNNING",
    "FINISHING",
    "FINISHED",
    "FAILING",
    "FAILED",
    "STOP_PENDING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookExecutionStatus:
    return cast(NotebookExecutionStatus, data)
