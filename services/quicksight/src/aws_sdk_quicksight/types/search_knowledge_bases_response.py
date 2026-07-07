"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base_summaries
    import aws_sdk_quicksight.types.next_token
    import aws_sdk_quicksight.types.status_code


class SearchKnowledgeBasesResponse(TypedDict, closed=True):
    knowledge_base_summaries: (
        "aws_sdk_quicksight.types.knowledge_base_summaries.KnowledgeBaseSummaries"
    )
    """<p>A list of knowledge base summaries.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.status_code.StatusCode"]
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.knowledge_base_summaries

    out["KnowledgeBaseSummaries"] = (
        aws_sdk_quicksight.types.knowledge_base_summaries.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchKnowledgeBasesResponse:
    out: SearchKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseSummaries" in data:
        import aws_sdk_quicksight.types.knowledge_base_summaries

        out["knowledge_base_summaries"] = (
            aws_sdk_quicksight.types.knowledge_base_summaries.deserialize_json(
                data["KnowledgeBaseSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "SearchKnowledgeBasesResponse.knowledge_base_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
