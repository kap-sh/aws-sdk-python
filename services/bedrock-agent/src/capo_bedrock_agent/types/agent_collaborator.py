"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaborator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_descriptor
    import capo_bedrock_agent.types.client_token
    import capo_bedrock_agent.types.collaboration_instruction
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.relay_conversation_history
    import capo_bedrock_agent.types.version


class AgentCollaborator(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's agent ID.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The collaborator's agent version.</p>"""
    agent_descriptor: "capo_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>The collaborator's agent descriptor.</p>"""
    collaborator_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's collaborator ID.</p>"""
    collaboration_instruction: (
        "capo_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>The collaborator's instructions.</p>"""
    collaborator_name: "capo_bedrock_agent.types.name.Name"
    """<p>The collaborator's collaborator name.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was created.</p>"""
    last_updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was updated.</p>"""
    relay_conversation_history: NotRequired[
        "capo_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    ]
    """<p>The collaborator's relay conversation history.</p>"""
    client_token: NotRequired["capo_bedrock_agent.types.client_token.ClientToken"]
    """<p>The collaborator's client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaborator) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    import capo_bedrock_agent.types.agent_descriptor

    out["agentDescriptor"] = capo_bedrock_agent.types.agent_descriptor.serialize_json(
        value["agent_descriptor"]
    )
    out["collaboratorId"] = value["collaborator_id"]
    out["collaborationInstruction"] = value["collaboration_instruction"]
    out["collaboratorName"] = value["collaborator_name"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["lastUpdatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["last_updated_at"]
    )
    if "relay_conversation_history" in value:
        import capo_bedrock_agent.types.relay_conversation_history

        out["relayConversationHistory"] = (
            capo_bedrock_agent.types.relay_conversation_history.serialize_json(
                value["relay_conversation_history"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AgentCollaborator:
    out: AgentCollaborator = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentCollaborator.agent_id required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentCollaborator.agent_version required")
    if "agentDescriptor" in data:
        import capo_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            capo_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError("AgentCollaborator.agent_descriptor required")
    if "collaboratorId" in data:
        out["collaborator_id"] = data["collaboratorId"]
    else:
        raise DeserializationError("AgentCollaborator.collaborator_id required")
    if "collaborationInstruction" in data:
        out["collaboration_instruction"] = data["collaborationInstruction"]
    else:
        raise DeserializationError(
            "AgentCollaborator.collaboration_instruction required"
        )
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        raise DeserializationError("AgentCollaborator.collaborator_name required")
    if "createdAt" in data:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentCollaborator.created_at required")
    if "lastUpdatedAt" in data:
        import capo_bedrock_agent.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agent.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("AgentCollaborator.last_updated_at required")
    if "relayConversationHistory" in data:
        import capo_bedrock_agent.types.relay_conversation_history

        out["relay_conversation_history"] = (
            capo_bedrock_agent.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
