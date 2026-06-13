"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version

class GetAgentRuntimeRequest(TypedDict):
    agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    """<p>The unique identifier of the AgentCore Runtime to retrieve.</p>"""
    agent_runtime_version: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"]
    """<p>The version of the AgentCore Runtime to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeRequest:
    out: GetAgentRuntimeRequest = {}  # type: ignore[typeddict-item]
    return out