"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_status
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.guardrail_configuration
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.version


class AgentVersionSummary(TypedDict, closed=True):
    agent_name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the agent to which the version belongs.</p>"""
    agent_status: "capo_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent to which the version belongs.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the version was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the version was last updated.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>The description of the version of the agent.</p>"""
    guardrail_configuration: NotRequired[
        "capo_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Details about the guardrail associated with the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentVersionSummary) -> dict:
    out: dict = {}
    out["agentName"] = value["agent_name"]
    import capo_bedrock_agent.types.agent_status

    out["agentStatus"] = capo_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    out["agentVersion"] = value["agent_version"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "guardrail_configuration" in value:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            capo_bedrock_agent.types.guardrail_configuration.serialize_json(
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
        import capo_bedrock_agent.types.agent_status

        out["agent_status"] = capo_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.agent_status required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentVersionSummary.agent_version required")
    if "createdAt" in data:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.created_at required")
    if "updatedAt" in data:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("AgentVersionSummary.updated_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "guardrailConfiguration" in data:
        import capo_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            capo_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    return out
