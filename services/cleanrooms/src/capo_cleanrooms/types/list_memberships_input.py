"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListMembershipsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.max_results
    import capo_cleanrooms.types.membership_status
    import capo_cleanrooms.types.pagination_token


class ListMembershipsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""
    max_results: NotRequired["capo_cleanrooms.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned for an API request call. The service chooses a default number if you don't set one. The service might return a `nextToken` even if the `maxResults` value has not been met.</p>"""
    status: NotRequired["capo_cleanrooms.types.membership_status.MembershipStatus"]
    """<p>A filter which will return only memberships in the specified status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMembershipsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMembershipsInput:
    out: ListMembershipsInput = {}  # type: ignore[typeddict-item]
    return out
