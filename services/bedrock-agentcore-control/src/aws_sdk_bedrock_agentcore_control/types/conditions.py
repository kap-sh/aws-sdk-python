"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.condition

Conditions: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.condition.Condition"
]


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> list:
    import aws_sdk_bedrock_agentcore_control.types.condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Conditions:
    import aws_sdk_bedrock_agentcore_control.types.condition

    out: Conditions = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.condition.deserialize_json(item)
        )
    return out
