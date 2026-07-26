"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TriggerConditionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.trigger_condition

TriggerConditionsList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.trigger_condition.TriggerCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConditionsList) -> list:
    import capo_bedrock_agentcore_control.types.trigger_condition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.trigger_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TriggerConditionsList:
    import capo_bedrock_agentcore_control.types.trigger_condition

    out: TriggerConditionsList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.trigger_condition.deserialize_json(
                item
            )
        )
    return out
