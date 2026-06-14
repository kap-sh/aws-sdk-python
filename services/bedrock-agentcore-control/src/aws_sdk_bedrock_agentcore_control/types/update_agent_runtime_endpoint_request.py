"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name


class UpdateAgentRuntimeEndpointRequest(TypedDict):
    agent_runtime_id: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to update.</p>"""
    agent_runtime_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The updated version of the AgentCore Runtime for the endpoint.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
    ]
    """<p>The updated description of the AgentCore Runtime endpoint.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    if "agent_runtime_version" in value:
        out["agentRuntimeVersion"] = value["agent_runtime_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateAgentRuntimeEndpointRequest:
    out: UpdateAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    if "agentRuntimeVersion" in data:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
