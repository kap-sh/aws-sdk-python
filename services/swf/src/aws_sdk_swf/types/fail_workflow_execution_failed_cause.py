"""Generated from Smithy shape ``com.amazonaws.swf#FailWorkflowExecutionFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

FailWorkflowExecutionFailedCause: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: FailWorkflowExecutionFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FailWorkflowExecutionFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FailWorkflowExecutionFailedCause value: {data!r}"
        )
    return cast(FailWorkflowExecutionFailedCause, data)
