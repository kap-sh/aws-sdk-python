"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name

class GetAgentRuntimeEndpointRequest(TypedDict):
    agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeEndpointRequest:
    out: GetAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    return out