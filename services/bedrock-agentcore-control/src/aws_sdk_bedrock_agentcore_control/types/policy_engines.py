"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyEngines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine

PolicyEngines: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.policy_engine.PolicyEngine"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEngines) -> list:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_engine.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PolicyEngines:
    import aws_sdk_bedrock_agentcore_control.types.policy_engine

    out: PolicyEngines = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.policy_engine.deserialize_json(item)
        )
    return out
