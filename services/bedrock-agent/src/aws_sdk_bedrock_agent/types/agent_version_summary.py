"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_status
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.version


class AgentVersionSummary(TypedDict, closed=True):
    agent_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the agent to which the version belongs.</p>"""
    agent_status: "aws_sdk_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent to which the version belongs.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The version of the agent.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the version was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the version was last updated.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the version of the agent.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Details about the guardrail associated with the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentVersionSummary) -> dict:
    out: dict = {}
    out["agentName"] = value["agent_name"]
    import aws_sdk_bedrock_agent.types.agent_status

    out["agentStatus"] = aws_sdk_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["agentVersion"] = value["agent_version"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentVersionSummary:
    out: AgentVersionSummary = {}  # type: ignore[typeddict-item]
    if "agentName" in data:
        out["agent_name"] = data["agentName"]
    else:
        raise DeserializationError("AgentVersionSummary.agent_name required")
    if "agentStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_status

        out["agent_status"] = aws_sdk_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.agent_status required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentVersionSummary.agent_version required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.updated_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    return out
