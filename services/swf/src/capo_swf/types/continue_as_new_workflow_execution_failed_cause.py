"""Generated from Smithy shape ``com.amazonaws.swf#ContinueAsNewWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

ContinueAsNewWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNHANDLED_DECISION",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContinueAsNewWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContinueAsNewWorkflowExecutionFailedCause:
    return cast(ContinueAsNewWorkflowExecutionFailedCause, data)
