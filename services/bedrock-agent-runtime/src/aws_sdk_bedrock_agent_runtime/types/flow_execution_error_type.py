"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionErrorType``."""

from typing import Literal, TypeAlias, cast

FlowExecutionErrorType: TypeAlias = Literal["ExecutionTimedOut",]


# --- restJson1 ser/de ---
def serialize_json(value: FlowExecutionErrorType) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionErrorType:
    return cast(FlowExecutionErrorType, data)
