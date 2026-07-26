"""Generated from Smithy shape ``com.amazonaws.groundstation#ListDataflowEndpointGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.pagination_max_results
    import capo_groundstation.types.pagination_token


class ListDataflowEndpointGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of dataflow endpoint groups returned.</p>"""
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token returned in the request of a previous <code>ListDataflowEndpointGroups</code> call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataflowEndpointGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataflowEndpointGroupsRequest:
    out: ListDataflowEndpointGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
