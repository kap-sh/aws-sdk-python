"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCancelRequestedCause``."""

from typing import Literal, TypeAlias, cast

WorkflowExecutionCancelRequestedCause: TypeAlias = Literal["CHILD_POLICY_APPLIED",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionCancelRequestedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionCancelRequestedCause:
    return cast(WorkflowExecutionCancelRequestedCause, data)
