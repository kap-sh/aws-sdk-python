"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentCollaboratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_collaborator


class GetAgentCollaboratorResponse(TypedDict, closed=True):
    agent_collaborator: "capo_bedrock_agent.types.agent_collaborator.AgentCollaborator"
    """<p>Details about the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentCollaboratorResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_collaborator

    out["agentCollaborator"] = (
        capo_bedrock_agent.types.agent_collaborator.serialize_json(
            value["agent_collaborator"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAgentCollaboratorResponse:
    out: GetAgentCollaboratorResponse = {}  # type: ignore[typeddict-item]
    if data.get("agentCollaborator") is not None:
        import capo_bedrock_agent.types.agent_collaborator

        out["agent_collaborator"] = (
            capo_bedrock_agent.types.agent_collaborator.deserialize_json(
                data["agentCollaborator"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentCollaboratorResponse.agent_collaborator required"
        )
    return out
