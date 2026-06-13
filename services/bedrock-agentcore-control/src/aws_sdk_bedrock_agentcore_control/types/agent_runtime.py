"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentRuntime``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_name
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.description

class AgentRuntime(TypedDict):
    agent_runtime_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the agent runtime.</p>"""
    agent_runtime_id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    """<p>The unique identifier of the agent runtime.</p>"""
    agent_runtime_version: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    """<p>The version of the agent runtime.</p>"""
    agent_runtime_name: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName"
    """<p>The name of the agent runtime.</p>"""
    description: "aws_sdk_bedrock_agentcore_control.types.description.Description"
    """<p>The description of the agent runtime.</p>"""
    last_updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the agent runtime was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    """<p>The current status of the agent runtime.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AgentRuntime) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
    out["agentRuntimeName"] = value["agent_runtime_name"]
    out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    out["lastUpdatedAt"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(value["last_updated_at"])
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> AgentRuntime:
    out: AgentRuntime = {}  # type: ignore[typeddict-item]
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError("AgentRuntime.agent_runtime_arn required")
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        raise DeserializationError("AgentRuntime.agent_runtime_id required")
    if "agentRuntimeVersion" in data:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        raise DeserializationError("AgentRuntime.agent_runtime_version required")
    if "agentRuntimeName" in data:
        out["agent_runtime_name"] = data["agentRuntimeName"]
    else:
        raise DeserializationError("AgentRuntime.agent_runtime_name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("AgentRuntime.description required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp
        out["last_updated_at"] = aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(data["lastUpdatedAt"])
    else:
        raise DeserializationError("AgentRuntime.last_updated_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("AgentRuntime.status required")
    return out