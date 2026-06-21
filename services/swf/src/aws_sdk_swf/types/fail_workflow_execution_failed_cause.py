"""Generated from Smithy shape ``com.amazonaws.swf#FailWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

FailWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNHANDLED_DECISION",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailWorkflowExecutionFailedCause:
    return cast(FailWorkflowExecutionFailedCause, data)
