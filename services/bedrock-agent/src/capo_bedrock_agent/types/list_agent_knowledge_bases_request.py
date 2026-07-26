"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentKnowledgeBasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token
    import capo_bedrock_agent.types.version


class ListAgentKnowledgeBasesRequest(TypedDict, closed=True):
    agent_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which to return information about knowledge bases associated with it.</p>"""
    agent_version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the agent for which to return information about knowledge bases associated with it.</p>"""
    max_results: NotRequired["capo_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentKnowledgeBasesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentKnowledgeBasesRequest:
    out: ListAgentKnowledgeBasesRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
