"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DisassociateAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.id


class DisassociateAgentCollaboratorRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>An agent ID.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The agent's version.</p>"""
    collaborator_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAgentCollaboratorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAgentCollaboratorRequest:
    out: DisassociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    return out
