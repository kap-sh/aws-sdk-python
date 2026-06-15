"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyMemoryStrategies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list
    import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list
    import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list


class ModifyMemoryStrategies(TypedDict):
    add_memory_strategies: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
    ]
    """<p>The list of memory strategies to add.</p>"""
    modify_memory_strategies: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list.ModifyMemoryStrategiesList"
    ]
    """<p>The list of memory strategies to modify.</p>"""
    delete_memory_strategies: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list.DeleteMemoryStrategiesList"
    ]
    """<p>The list of memory strategies to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyMemoryStrategies) -> dict:
    out: dict = {}
    if "add_memory_strategies" in value:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list

        out["addMemoryStrategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.serialize_json(
                value["add_memory_strategies"]
            )
        )
    if "modify_memory_strategies" in value:
        import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list

        out["modifyMemoryStrategies"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list.serialize_json(
                value["modify_memory_strategies"]
            )
        )
    if "delete_memory_strategies" in value:
        import aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list

        out["deleteMemoryStrategies"] = (
            aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list.serialize_json(
                value["delete_memory_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModifyMemoryStrategies:
    out: ModifyMemoryStrategies = {}  # type: ignore[typeddict-item]
    if "addMemoryStrategies" in data:
        import aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list

        out["add_memory_strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.memory_strategy_input_list.deserialize_json(
                data["addMemoryStrategies"]
            )
        )
    if "modifyMemoryStrategies" in data:
        import aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list

        out["modify_memory_strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.modify_memory_strategies_list.deserialize_json(
                data["modifyMemoryStrategies"]
            )
        )
    if "deleteMemoryStrategies" in data:
        import aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list

        out["delete_memory_strategies"] = (
            aws_sdk_bedrock_agentcore_control.types.delete_memory_strategies_list.deserialize_json(
                data["deleteMemoryStrategies"]
            )
        )
    return out
