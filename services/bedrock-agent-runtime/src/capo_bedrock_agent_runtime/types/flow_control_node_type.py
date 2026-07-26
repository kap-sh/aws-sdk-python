"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowControlNodeType``."""

from typing import Literal, TypeAlias, cast

FlowControlNodeType: TypeAlias = Literal[
    "Iterator",
    "Loop",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowControlNodeType) -> str:
    return value


def deserialize_json(data: str) -> FlowControlNodeType:
    return cast(FlowControlNodeType, data)
