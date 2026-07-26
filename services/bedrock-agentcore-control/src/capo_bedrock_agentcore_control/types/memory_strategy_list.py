"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MemoryStrategyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory_strategy

MemoryStrategyList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.memory_strategy.MemoryStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryStrategyList) -> list:
    import capo_bedrock_agentcore_control.types.memory_strategy

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.memory_strategy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MemoryStrategyList:
    import capo_bedrock_agentcore_control.types.memory_strategy

    out: MemoryStrategyList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.memory_strategy.deserialize_json(item)
        )
    return out
