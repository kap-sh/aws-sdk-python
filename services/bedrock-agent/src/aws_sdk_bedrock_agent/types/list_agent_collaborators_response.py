"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentCollaboratorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_collaborator_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListAgentCollaboratorsResponse(TypedDict):
    agent_collaborator_summaries: "aws_sdk_bedrock_agent.types.agent_collaborator_summaries.AgentCollaboratorSummaries"
    """<p>A list of collaborator summaries.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentCollaboratorsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_collaborator_summaries

    out["agentCollaboratorSummaries"] = (
        aws_sdk_bedrock_agent.types.agent_collaborator_summaries.serialize_json(
            value["agent_collaborator_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentCollaboratorsResponse:
    out: ListAgentCollaboratorsResponse = {}  # type: ignore[typeddict-item]
    if "agentCollaboratorSummaries" in data:
        import aws_sdk_bedrock_agent.types.agent_collaborator_summaries

        out["agent_collaborator_summaries"] = (
            aws_sdk_bedrock_agent.types.agent_collaborator_summaries.deserialize_json(
                data["agentCollaboratorSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgentCollaboratorsResponse.agent_collaborator_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
