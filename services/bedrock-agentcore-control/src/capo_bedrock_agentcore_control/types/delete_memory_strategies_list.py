"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryStrategiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.delete_memory_strategy_input

DeleteMemoryStrategiesList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.delete_memory_strategy_input.DeleteMemoryStrategyInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryStrategiesList) -> list:
    import capo_bedrock_agentcore_control.types.delete_memory_strategy_input

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.delete_memory_strategy_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeleteMemoryStrategiesList:
    import capo_bedrock_agentcore_control.types.delete_memory_strategy_input

    out: DeleteMemoryStrategiesList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.delete_memory_strategy_input.deserialize_json(
                item
            )
        )
    return out
