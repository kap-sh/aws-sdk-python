"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input

MemoryStrategyInputList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.memory_strategy_input.MemoryStrategyInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyInputList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MemoryStrategyInputList:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input

    out: MemoryStrategyInputList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input.deserialize_json(
                item
            )
        )
    return out
