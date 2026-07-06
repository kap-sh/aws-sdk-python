"""Generated from Smithy shape ``com.amazonaws.wisdom#ListKnowledgeBasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.non_empty_string


class ListKnowledgeBasesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesRequest:
    out: ListKnowledgeBasesRequest = {}  # type: ignore[typeddict-item]
    return out
