"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AssociateAgentCollaboratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_collaborator


class AssociateAgentCollaboratorResponse(TypedDict, closed=True):
    agent_collaborator: (
        "aws_sdk_bedrock_agent.types.agent_collaborator.AgentCollaborator"
    )
    """<p>Details about the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAgentCollaboratorResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_collaborator

    out["agentCollaborator"] = (
        aws_sdk_bedrock_agent.types.agent_collaborator.serialize_json(
            value["agent_collaborator"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateAgentCollaboratorResponse:
    out: AssociateAgentCollaboratorResponse = {}  # type: ignore[typeddict-item]
    if "agentCollaborator" in data:
        import aws_sdk_bedrock_agent.types.agent_collaborator

        out["agent_collaborator"] = (
            aws_sdk_bedrock_agent.types.agent_collaborator.deserialize_json(
                data["agentCollaborator"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateAgentCollaboratorResponse.agent_collaborator required"
        )
    return out
