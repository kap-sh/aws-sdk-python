"""Generated from Smithy shape ``com.amazonaws.transfer#WorkflowStepType``."""

from typing import Literal, TypeAlias, cast

WorkflowStepType: TypeAlias = Literal[
    "COPY",
    "CUSTOM",
    "TAG",
    "DELETE",
    "DECRYPT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowStepType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkflowStepType:
    return cast(WorkflowStepType, data)
