"""Generated from Smithy shape ``com.amazonaws.quicksight#ListKnowledgeBasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kb_aws_account_id
    import capo_quicksight.types.max_results
    import capo_quicksight.types.next_token


class ListKnowledgeBasesRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.kb_aws_account_id.KbAwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the knowledge base.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesRequest:
    out: ListKnowledgeBasesRequest = {}  # type: ignore[typeddict-item]
    return out
