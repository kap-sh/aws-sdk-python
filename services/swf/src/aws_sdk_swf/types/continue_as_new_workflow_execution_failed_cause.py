"""Generated from Smithy shape ``com.amazonaws.swf#ContinueAsNewWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "UNHANDLED_DECISION",
        "WORKFLOW_TYPE_DEPRECATED",
        "WORKFLOW_TYPE_DOES_NOT_EXIST",
        "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_LIST_UNDEFINED",
        "DEFAULT_CHILD_POLICY_UNDEFINED",
        "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: ContinueAsNewWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContinueAsNewWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContinueAsNewWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(ContinueAsNewWorkflowExecutionFailedCause, data)
