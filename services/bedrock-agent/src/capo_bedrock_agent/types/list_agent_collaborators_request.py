"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentCollaboratorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.version


class ListAgentCollaboratorsRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The agent's ID.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The agent's version.</p>"""
    max_results: NotRequired["capo_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of agent collaborators to return in one page of results.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentCollaboratorsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentCollaboratorsRequest:
    out: ListAgentCollaboratorsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
