"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyMemoryStrategiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input

ModifyMemoryStrategiesList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input.ModifyMemoryStrategyInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModifyMemoryStrategiesList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ModifyMemoryStrategiesList:
    import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input

    out: ModifyMemoryStrategiesList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.modify_memory_strategy_input.deserialize_json(
                item
            )
        )
    return out
