"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowExecutionErrorType: TypeAlias = Literal["ExecutionTimedOut",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ExecutionTimedOut",))


def serialize_json(value: FlowExecutionErrorType) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionErrorType value: {data!r}")
    return cast(FlowExecutionErrorType, data)
