"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_status
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.version


class AgentSummary(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the agent.</p>"""
    agent_status: "aws_sdk_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the agent.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the agent was last updated.</p>"""
    latest_agent_version: NotRequired["aws_sdk_bedrock_agent.types.version.Version"]
    """<p>The latest version of the agent.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Details about the guardrail associated with the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummary) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentName"] = value["agent_name"]
    import aws_sdk_bedrock_agent.types.agent_status

    out["agentStatus"] = aws_sdk_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "latest_agent_version" in value:
        out["latestAgentVersion"] = value["latest_agent_version"]
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSummary:
    out: AgentSummary = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentSummary.agent_id required")
    if "agentName" in data:
        out["agent_name"] = data["agentName"]
    else:
        raise DeserializationError("AgentSummary.agent_name required")
    if "agentStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_status

        out["agent_status"] = aws_sdk_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("AgentSummary.agent_status required")
    if "description" in data:
        out["description"] = data["description"]
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentSummary.updated_at required")
    if "latestAgentVersion" in data:
        out["latest_agent_version"] = data["latestAgentVersion"]
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    return out
