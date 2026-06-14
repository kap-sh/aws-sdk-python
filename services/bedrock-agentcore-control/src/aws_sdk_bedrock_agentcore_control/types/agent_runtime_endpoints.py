"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint

AgentRuntimeEndpoints: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint.AgentRuntimeEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeEndpoints) -> list:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentRuntimeEndpoints:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint

    out: AgentRuntimeEndpoints = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint.deserialize_json(
                item
            )
        )
    return out
