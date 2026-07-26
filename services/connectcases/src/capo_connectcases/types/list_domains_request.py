"""Generated from Smithy shape ``com.amazonaws.connectcases#ListDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.max_results
    import capo_connectcases.types.next_token


class ListDomainsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_connectcases.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    return out
