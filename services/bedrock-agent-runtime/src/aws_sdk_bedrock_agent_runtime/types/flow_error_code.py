"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowErrorCode``."""

from typing import Literal, TypeAlias, cast

FlowErrorCode: TypeAlias = Literal[
    "VALIDATION",
    "INTERNAL_SERVER",
    "NODE_EXECUTION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowErrorCode) -> str:
    return value


def deserialize_json(data: str) -> FlowErrorCode:
    return cast(FlowErrorCode, data)
