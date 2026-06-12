"""Generated from Smithy shape ``com.amazonaws.swf#CancelWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

CancelWorkflowExecutionFailedCause: TypeAlias = Literal[
    "UNHANDLED_DECISION",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNHANDLED_DECISION",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: CancelWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CancelWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CancelWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(CancelWorkflowExecutionFailedCause, data)
