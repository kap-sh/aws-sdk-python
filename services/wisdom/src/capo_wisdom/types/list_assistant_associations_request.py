"""Generated from Smithy shape ``com.amazonaws.wisdom#ListAssistantAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.max_results
    import capo_wisdom.types.next_token
    import capo_wisdom.types.uuid_or_arn


class ListAssistantAssociationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_wisdom.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssistantAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssistantAssociationsRequest:
    out: ListAssistantAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
