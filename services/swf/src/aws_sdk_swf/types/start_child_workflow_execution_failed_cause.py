"""Generated from Smithy shape ``com.amazonaws.swf#StartChildWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

StartChildWorkflowExecutionFailedCause: TypeAlias = Literal[
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
    "WORKFLOW_TYPE_DEPRECATED",
    "OPEN_CHILDREN_LIMIT_EXCEEDED",
    "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
    "CHILD_CREATION_RATE_EXCEEDED",
    "WORKFLOW_ALREADY_RUNNING",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WORKFLOW_TYPE_DOES_NOT_EXIST",
        "WORKFLOW_TYPE_DEPRECATED",
        "OPEN_CHILDREN_LIMIT_EXCEEDED",
        "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
        "CHILD_CREATION_RATE_EXCEEDED",
        "WORKFLOW_ALREADY_RUNNING",
        "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_TASK_LIST_UNDEFINED",
        "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
        "DEFAULT_CHILD_POLICY_UNDEFINED",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: StartChildWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StartChildWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StartChildWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(StartChildWorkflowExecutionFailedCause, data)
