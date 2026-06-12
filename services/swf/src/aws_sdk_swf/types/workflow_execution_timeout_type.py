"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTimeoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

WorkflowExecutionTimeoutType: TypeAlias = Literal["START_TO_CLOSE",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("START_TO_CLOSE",))


def serialize_aws_json_1_0(value: WorkflowExecutionTimeoutType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkflowExecutionTimeoutType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkflowExecutionTimeoutType value: {data!r}"
        )
    return cast(WorkflowExecutionTimeoutType, data)
