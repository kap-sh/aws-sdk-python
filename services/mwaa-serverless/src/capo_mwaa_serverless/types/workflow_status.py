"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowStatus: TypeAlias = Literal[
    "READY",
    "DELETING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowStatus:
    return cast(WorkflowStatus, data)
