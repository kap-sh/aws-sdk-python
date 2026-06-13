"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntimeEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name

class AgentRuntimeEndpoint(TypedDict):
    name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the agent runtime endpoint.</p>"""
    live_version: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"]
    """<p>The live version of the agent runtime endpoint. This is the version that is currently serving requests.</p>"""
    target_version: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"]
    """<p>The target version of the agent runtime endpoint. This is the version that the endpoint is being updated to.</p>"""
    agent_runtime_endpoint_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime endpoint.</p>"""
    agent_runtime_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime associated with the endpoint.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the agent runtime endpoint.</p>"""
    id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_id.AgentRuntimeEndpointId"
    """<p>The unique identifier of the agent runtime endpoint.</p>"""
    description: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"]
    """<p>The description of the agent runtime endpoint.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime endpoint was created.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime endpoint was last updated.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntimeEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "live_version" in value:
        out["liveVersion"] = value["live_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(value["status"])
    out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["createdAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["created_at"])
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["lastUpdatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["last_updated_at"])
    return out


def deserialize_json(data: dict) -> AgentRuntimeEndpoint:
    out: AgentRuntimeEndpoint = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AgentRuntimeEndpoint.name required")
    if "liveVersion" in data:
        out["live_version"] = data["liveVersion"]
    if "targetVersion" in data:
        out["target_version"] = data["targetVersion"]
    if "agentRuntimeEndpointArn" in data:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        raise DeserializationError("AgentRuntimeEndpoint.agent_runtime_endpoint_arn required")
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError("AgentRuntimeEndpoint.agent_runtime_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("AgentRuntimeEndpoint.status required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AgentRuntimeEndpoint.id required")
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["created_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["createdAt"])
    else:
        raise DeserializationError("AgentRuntimeEndpoint.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["last_updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["lastUpdatedAt"])
    else:
        raise DeserializationError("AgentRuntimeEndpoint.last_updated_at required")
    return out