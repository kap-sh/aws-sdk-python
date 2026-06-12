"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentCollaboratorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_collaborator


class UpdateAgentCollaboratorResponse(TypedDict):
    agent_collaborator: (
        "aws_sdk_bedrock_agent.types.agent_collaborator.AgentCollaborator"
    )
    """<p>Details about the collaborator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentCollaboratorResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_collaborator

    out["agentCollaborator"] = (
        aws_sdk_bedrock_agent.types.agent_collaborator.serialize_json(
            value["agent_collaborator"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentCollaboratorResponse:
    out: UpdateAgentCollaboratorResponse = {}  # type: ignore[typeddict-item]
    if "agentCollaborator" in data:
        import aws_sdk_bedrock_agent.types.agent_collaborator

        out["agent_collaborator"] = (
            aws_sdk_bedrock_agent.types.agent_collaborator.deserialize_json(
                data["agentCollaborator"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentCollaboratorResponse.agent_collaborator required"
        )
    return out
