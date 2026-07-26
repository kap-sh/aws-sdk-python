"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelExternalWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

RequestCancelExternalWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: RequestCancelExternalWorkflowExecutionFailedCause,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> RequestCancelExternalWorkflowExecutionFailedCause:
    return cast(RequestCancelExternalWorkflowExecutionFailedCause, data)
