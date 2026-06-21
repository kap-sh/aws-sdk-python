"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTerminatedCause``."""

from typing import Literal, TypeAlias, cast

WorkflowExecutionTerminatedCause: TypeAlias = Literal[
    "CHILD_POLICY_APPLIED",
    "EVENT_LIMIT_EXCEEDED",
    "OPERATOR_INITIATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionTerminatedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionTerminatedCause:
    return cast(WorkflowExecutionTerminatedCause, data)
