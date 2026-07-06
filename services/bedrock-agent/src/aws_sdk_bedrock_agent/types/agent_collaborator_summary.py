"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentCollaboratorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_descriptor
    import aws_sdk_bedrock_agent.types.collaboration_instruction
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.relay_conversation_history
    import aws_sdk_bedrock_agent.types.version


class AgentCollaboratorSummary(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The collaborator's agent ID.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The collaborator's agent version.</p>"""
    collaborator_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""
    agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>The collaborator's agent descriptor.</p>"""
    collaboration_instruction: (
        "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>The collaborator's collaboration instruction.</p>"""
    relay_conversation_history: "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    """<p>The collaborator's relay conversation history.</p>"""
    collaborator_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The collaborator's name.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was created.</p>"""
    last_updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>When the collaborator was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentCollaboratorSummary) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentVersion"] = value["agent_version"]
    out["collaboratorId"] = value["collaborator_id"]
    import aws_sdk_bedrock_agent.types.agent_descriptor

    out["agentDescriptor"] = (
        aws_sdk_bedrock_agent.types.agent_descriptor.serialize_json(
            value["agent_descriptor"]
        )
    )
    out["collaborationInstruction"] = value["collaboration_instruction"]
    import aws_sdk_bedrock_agent.types.relay_conversation_history

    out["relayConversationHistory"] = (
        aws_sdk_bedrock_agent.types.relay_conversation_history.serialize_json(
            value["relay_conversation_history"]
        )
    )
    out["collaboratorName"] = value["collaborator_name"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["lastUpdatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AgentCollaboratorSummary:
    out: AgentCollaboratorSummary = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("AgentCollaboratorSummary.agent_id required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("AgentCollaboratorSummary.agent_version required")
    if "collaboratorId" in data:
        out["collaborator_id"] = data["collaboratorId"]
    else:
        raise DeserializationError("AgentCollaboratorSummary.collaborator_id required")
    if "agentDescriptor" in data:
        import aws_sdk_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            aws_sdk_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError("AgentCollaboratorSummary.agent_descriptor required")
    if "collaborationInstruction" in data:
        out["collaboration_instruction"] = data["collaborationInstruction"]
    else:
        raise DeserializationError(
            "AgentCollaboratorSummary.collaboration_instruction required"
        )
    if "relayConversationHistory" in data:
        import aws_sdk_bedrock_agent.types.relay_conversation_history

        out["relay_conversation_history"] = (
            aws_sdk_bedrock_agent.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    else:
        raise DeserializationError(
            "AgentCollaboratorSummary.relay_conversation_history required"
        )
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        raise DeserializationError(
            "AgentCollaboratorSummary.collaborator_name required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AgentCollaboratorSummary.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("AgentCollaboratorSummary.last_updated_at required")
    return out
