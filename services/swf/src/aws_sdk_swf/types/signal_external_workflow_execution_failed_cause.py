"""Generated from Smithy shape ``com.amazonaws.swf#SignalExternalWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

SignalExternalWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalExternalWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalExternalWorkflowExecutionFailedCause:
    return cast(SignalExternalWorkflowExecutionFailedCause, data)
