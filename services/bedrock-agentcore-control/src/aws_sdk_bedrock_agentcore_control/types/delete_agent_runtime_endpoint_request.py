"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteAgentRuntimeEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name


class DeleteAgentRuntimeEndpointRequest(TypedDict):
    agent_runtime_id: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>"""
    endpoint_name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint to delete.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRuntimeEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentRuntimeEndpointRequest:
    out: DeleteAgentRuntimeEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
