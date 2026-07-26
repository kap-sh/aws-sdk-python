"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionEventType``."""

from typing import Literal, TypeAlias, cast

FlowExecutionEventType: TypeAlias = Literal[
    "Node",
    "Flow",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionEventType) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionEventType:
    return cast(FlowExecutionEventType, data)
