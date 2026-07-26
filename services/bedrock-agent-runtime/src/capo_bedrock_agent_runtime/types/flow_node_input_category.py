"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowNodeInputCategory``."""

from typing import Literal, TypeAlias, cast

FlowNodeInputCategory: TypeAlias = Literal[
    "LoopCondition",
    "ReturnValueToLoopStart",
    "ExitLoop",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeInputCategory) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeInputCategory:
    return cast(FlowNodeInputCategory, data)
