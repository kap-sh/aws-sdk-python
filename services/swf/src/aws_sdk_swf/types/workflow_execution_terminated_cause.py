"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTerminatedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

WorkflowExecutionTerminatedCause: TypeAlias = Literal[
    "CHILD_POLICY_APPLIED",
    "EVENT_LIMIT_EXCEEDED",
    "OPERATOR_INITIATED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHILD_POLICY_APPLIED",
        "EVENT_LIMIT_EXCEEDED",
        "OPERATOR_INITIATED",
    )
)


def serialize_aws_json_1_0(value: WorkflowExecutionTerminatedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionTerminatedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkflowExecutionTerminatedCause value: {data!r}"
        )
    return cast(WorkflowExecutionTerminatedCause, data)
