"""Generated from Smithy shape ``com.amazonaws.swf#CompleteWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

CompleteWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNHANDLED_DECISION",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompleteWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CompleteWorkflowExecutionFailedCause:
    return cast(CompleteWorkflowExecutionFailedCause, data)
