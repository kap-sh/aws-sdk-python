"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_descriptor
    import aws_sdk_bedrock_agent.types.collaboration_instruction
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.relay_conversation_history


class UpdateAgentCollaboratorRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The agent's ID.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The agent's version.</p>"""
    collaborator_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""
    agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>An agent descriptor for the agent collaborator.</p>"""
    collaborator_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The collaborator's name.</p>"""
    collaboration_instruction: (
        "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>Instruction for the collaborator.</p>"""
    relay_conversation_history: NotRequired[
        "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    ]
    """<p>A relay conversation history for the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentCollaboratorRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_descriptor

    out["agentDescriptor"] = (
        aws_sdk_bedrock_agent.types.agent_descriptor.serialize_json(
            value["agent_descriptor"]
        )
    )
    out["collaboratorName"] = value["collaborator_name"]
    out["collaborationInstruction"] = value["collaboration_instruction"]
    if "relay_conversation_history" in value:
        import aws_sdk_bedrock_agent.types.relay_conversation_history

        out["relayConversationHistory"] = (
            aws_sdk_bedrock_agent.types.relay_conversation_history.serialize_json(
                value["relay_conversation_history"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentCollaboratorRequest:
    out: UpdateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    if "agentDescriptor" in data:
        import aws_sdk_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            aws_sdk_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentCollaboratorRequest.agent_descriptor required"
        )
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        raise DeserializationError(
            "UpdateAgentCollaboratorRequest.collaborator_name required"
        )
    if "collaborationInstruction" in data:
        out["collaboration_instruction"] = data["collaborationInstruction"]
    else:
        raise DeserializationError(
            "UpdateAgentCollaboratorRequest.collaboration_instruction required"
        )
    if "relayConversationHistory" in data:
        import aws_sdk_bedrock_agent.types.relay_conversation_history

        out["relay_conversation_history"] = (
            aws_sdk_bedrock_agent.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    return out
