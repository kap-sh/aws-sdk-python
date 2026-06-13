"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowExecutionEventType: TypeAlias = Literal[
    "Node",
    "Flow",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Node",
        "Flow",
    )
)


def serialize_json(value: FlowExecutionEventType) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionEventType value: {data!r}")
    return cast(FlowExecutionEventType, data)
