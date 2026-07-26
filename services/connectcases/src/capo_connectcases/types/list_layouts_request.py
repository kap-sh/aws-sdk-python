"""Generated from Smithy shape ``com.amazonaws.connectcases#ListLayoutsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token


class ListLayoutsRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    max_results: NotRequired["capo_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLayoutsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLayoutsRequest:
    out: ListLayoutsRequest = {}  # type: ignore[typeddict-item]
    return out
