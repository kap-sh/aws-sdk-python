"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.policy

Policies: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: Policies) -> list:
    import aws_sdk_bedrock_agentcore_control.types.policy

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Policies:
    import aws_sdk_bedrock_agentcore_control.types.policy

    out: Policies = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy.deserialize_json(item)
        )
    return out
