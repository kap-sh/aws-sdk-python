"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareAgentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_status
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.version


class PrepareAgentResponse(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which the <code>DRAFT</code> version was created.</p>"""
    agent_status: "aws_sdk_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the <code>DRAFT</code> version and whether it is ready for use.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The version of the agent.</p>"""
    prepared_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the <code>DRAFT</code> version of the agent was last prepared.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareAgentResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    import aws_sdk_bedrock_agent.types.agent_status

    out["agentStatus"] = aws_sdk_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["agentVersion"] = value["agent_version"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["preparedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["prepared_at"]
    )
    return out


def deserialize_json(data: dict) -> PrepareAgentResponse:
    out: PrepareAgentResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("PrepareAgentResponse.agent_id required")
    if "agentStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_status

        out["agent_status"] = aws_sdk_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("PrepareAgentResponse.agent_status required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("PrepareAgentResponse.agent_version required")
    if "preparedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["prepared_at"] = (
            aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
                data["preparedAt"]
            )
        )
    else:
        raise DeserializationError("PrepareAgentResponse.prepared_at required")
    return out
