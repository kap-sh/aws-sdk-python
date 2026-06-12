"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AssociateAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_descriptor
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.collaboration_instruction
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.relay_conversation_history


class AssociateAgentCollaboratorRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The agent's ID.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>An agent version.</p>"""
    agent_descriptor: "aws_sdk_bedrock_agent.types.agent_descriptor.AgentDescriptor"
    """<p>The alias of the collaborator agent.</p>"""
    collaborator_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>A name for the collaborator.</p>"""
    collaboration_instruction: (
        "aws_sdk_bedrock_agent.types.collaboration_instruction.CollaborationInstruction"
    )
    """<p>Instruction for the collaborator.</p>"""
    relay_conversation_history: NotRequired[
        "aws_sdk_bedrock_agent.types.relay_conversation_history.RelayConversationHistory"
    ]
    """<p>A relay conversation history for the collaborator.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAgentCollaboratorRequest) -> dict:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateAgentCollaboratorRequest:
    out: AssociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    if "agentDescriptor" in data:
        import aws_sdk_bedrock_agent.types.agent_descriptor

        out["agent_descriptor"] = (
            aws_sdk_bedrock_agent.types.agent_descriptor.deserialize_json(
                data["agentDescriptor"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateAgentCollaboratorRequest.agent_descriptor required"
        )
    if "collaboratorName" in data:
        out["collaborator_name"] = data["collaboratorName"]
    else:
        raise DeserializationError(
            "AssociateAgentCollaboratorRequest.collaborator_name required"
        )
    if "collaborationInstruction" in data:
        out["collaboration_instruction"] = data["collaborationInstruction"]
    else:
        raise DeserializationError(
            "AssociateAgentCollaboratorRequest.collaboration_instruction required"
        )
    if "relayConversationHistory" in data:
        import aws_sdk_bedrock_agent.types.relay_conversation_history

        out["relay_conversation_history"] = (
            aws_sdk_bedrock_agent.types.relay_conversation_history.deserialize_json(
                data["relayConversationHistory"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
