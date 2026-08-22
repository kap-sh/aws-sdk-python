"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListKnowledgeBaseDocumentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.id
    import capo_bedrock_agent.types.max_results
    import capo_bedrock_agent.types.next_token


class ListKnowledgeBaseDocumentsRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the knowledge base that is connected to the data source.</p>"""
    data_source_id: "capo_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the data source that contains the documents.</p>"""
    max_results: NotRequired["capo_bedrock_agent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBaseDocumentsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBaseDocumentsRequest:
    out: ListKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
