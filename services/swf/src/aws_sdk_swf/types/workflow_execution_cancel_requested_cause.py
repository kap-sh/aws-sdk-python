"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionCancelRequestedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

WorkflowExecutionCancelRequestedCause: TypeAlias = Literal["CHILD_POLICY_APPLIED",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CHILD_POLICY_APPLIED",))


def serialize_aws_json_1_0(value: WorkflowExecutionCancelRequestedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionCancelRequestedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkflowExecutionCancelRequestedCause value: {data!r}"
        )
    return cast(WorkflowExecutionCancelRequestedCause, data)
