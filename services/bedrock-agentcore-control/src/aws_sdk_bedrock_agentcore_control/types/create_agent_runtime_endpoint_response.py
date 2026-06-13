"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateAgentRuntimeEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name

class CreateAgentRuntimeEndpointResponse(TypedDict):
    target_version: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    """<p>The target version of the AgentCore Runtime for the endpoint.</p>"""
    agent_runtime_endpoint_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.</p>"""
    agent_runtime_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    agent_runtime_id: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"]
    """<p>The unique identifier of the AgentCore Runtime.</p>"""
    endpoint_name: NotRequired["aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"]
    """<p>The name of the AgentCore Runtime endpoint.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the AgentCore Runtime endpoint.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime endpoint was created.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRuntimeEndpointResponse) -> dict:
    out: dict = {}
    out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    if "agent_runtime_id" in value:
        out["agentRuntimeId"] = value["agent_runtime_id"]
    if "endpoint_name" in value:
        out["endpointName"] = value["endpoint_name"]
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(value["status"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> CreateAgentRuntimeEndpointResponse:
    out: CreateAgentRuntimeEndpointResponse = {}  # type: ignore[typeddict-item]
    if "targetVersion" in data:
        out["target_version"] = data["targetVersion"]
    else:
        raise DeserializationError("CreateAgentRuntimeEndpointResponse.target_version required")
    if "agentRuntimeEndpointArn" in data:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        raise DeserializationError("CreateAgentRuntimeEndpointResponse.agent_runtime_endpoint_arn required")
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError("CreateAgentRuntimeEndpointResponse.agent_runtime_arn required")
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    if "endpointName" in data:
        out["endpoint_name"] = data["endpointName"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("CreateAgentRuntimeEndpointResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("CreateAgentRuntimeEndpointResponse.created_at required")
    return out