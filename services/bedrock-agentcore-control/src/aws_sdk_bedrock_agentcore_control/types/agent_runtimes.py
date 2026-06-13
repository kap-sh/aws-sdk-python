"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime

AgentRuntimes: TypeAlias = list["aws_sdk_bedrock_agentcore_control.types.agent_runtime.AgentRuntime"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimes) -> list:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore_control.types.agent_runtime.serialize_json(item))
    return out


def deserialize_json(data: list) -> AgentRuntimes:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime
    out: AgentRuntimes = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore_control.types.agent_runtime.deserialize_json(item))
    return out