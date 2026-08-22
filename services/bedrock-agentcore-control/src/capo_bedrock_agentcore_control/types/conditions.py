"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.condition

Conditions: TypeAlias = list["capo_bedrock_agentcore_control.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> list:
    import capo_bedrock_agentcore_control.types.condition

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore_control.types.condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Conditions:
    import capo_bedrock_agentcore_control.types.condition

    out: Conditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.condition.deserialize_json(item)
        )
    return out
