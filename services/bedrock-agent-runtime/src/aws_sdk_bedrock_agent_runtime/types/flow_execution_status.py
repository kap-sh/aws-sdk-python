"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

FlowExecutionStatus: TypeAlias = Literal[
    "Running",
    "Succeeded",
    "Failed",
    "TimedOut",
    "Aborted",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionStatus:
    return cast(FlowExecutionStatus, data)
