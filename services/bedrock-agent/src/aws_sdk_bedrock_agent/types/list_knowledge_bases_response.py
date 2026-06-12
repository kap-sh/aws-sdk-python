"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListKnowledgeBasesResponse(TypedDict):
    knowledge_base_summaries: (
        "aws_sdk_bedrock_agent.types.knowledge_base_summaries.KnowledgeBaseSummaries"
    )
    """<p>A list of knowledge bases with information about each knowledge base.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.knowledge_base_summaries

    out["knowledgeBaseSummaries"] = (
        aws_sdk_bedrock_agent.types.knowledge_base_summaries.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesResponse:
    out: ListKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseSummaries" in data:
        import aws_sdk_bedrock_agent.types.knowledge_base_summaries

        out["knowledge_base_summaries"] = (
            aws_sdk_bedrock_agent.types.knowledge_base_summaries.deserialize_json(
                data["knowledgeBaseSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListKnowledgeBasesResponse.knowledge_base_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
