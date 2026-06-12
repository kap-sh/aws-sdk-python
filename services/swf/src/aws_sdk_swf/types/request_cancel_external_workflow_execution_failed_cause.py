"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelExternalWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

RequestCancelExternalWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
        "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(
    value: RequestCancelExternalWorkflowExecutionFailedCause,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> RequestCancelExternalWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RequestCancelExternalWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(RequestCancelExternalWorkflowExecutionFailedCause, data)
