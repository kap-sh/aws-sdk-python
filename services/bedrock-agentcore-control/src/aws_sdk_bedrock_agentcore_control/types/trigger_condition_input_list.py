"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TriggerConditionInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input

TriggerConditionInputList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.trigger_condition_input.TriggerConditionInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerConditionInputList) -> list:
    import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.trigger_condition_input.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TriggerConditionInputList:
    import aws_sdk_bedrock_agentcore_control.types.trigger_condition_input

    out: TriggerConditionInputList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.trigger_condition_input.deserialize_json(
                item
            )
        )
    return out
