"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy

MemoryStrategyList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.memory_strategy.MemoryStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_strategy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryStrategyList:
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy

    out: MemoryStrategyList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.memory_strategy.deserialize_json(
                item
            )
        )
    return out
