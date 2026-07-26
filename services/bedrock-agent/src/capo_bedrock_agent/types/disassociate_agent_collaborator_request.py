"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DisassociateAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.draft_version
    import capo_bedrock_agent.types.id


class DisassociateAgentCollaboratorRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>An agent ID.</p>"""
    agent_version: "capo_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The agent's version.</p>"""
    collaborator_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAgentCollaboratorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateAgentCollaboratorRequest:
    out: DisassociateAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    return out
