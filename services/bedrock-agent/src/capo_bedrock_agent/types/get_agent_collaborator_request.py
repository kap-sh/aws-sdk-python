"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentCollaboratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.version


class GetAgentCollaboratorRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The agent's ID.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The agent's version.</p>"""
    collaborator_id: "capo_bedrock_agent.types.id.Id"
    """<p>The collaborator's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentCollaboratorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentCollaboratorRequest:
    out: GetAgentCollaboratorRequest = {}  # type: ignore[typeddict-item]
    return out
