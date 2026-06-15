"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation

PolicyGenerations: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.policy_generation.PolicyGeneration"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerations) -> list:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_generation.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PolicyGenerations:
    import aws_sdk_bedrock_agentcore_control.types.policy_generation

    out: PolicyGenerations = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_generation.deserialize_json(
                item
            )
        )
    return out
