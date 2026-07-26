"""Generated from Smithy shape ``com.amazonaws.swf#CancelWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

CancelWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNHANDLED_DECISION",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CancelWorkflowExecutionFailedCause:
    return cast(CancelWorkflowExecutionFailedCause, data)
