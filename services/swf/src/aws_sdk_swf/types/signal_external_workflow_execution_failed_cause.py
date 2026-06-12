"""Generated from Smithy shape ``com.amazonaws.swf#SignalExternalWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

SignalExternalWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
    "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
        "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: SignalExternalWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SignalExternalWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SignalExternalWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(SignalExternalWorkflowExecutionFailedCause, data)
