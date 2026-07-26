"""Generated from Smithy shape ``com.amazonaws.mgn#ListManagedAccountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListManagedAccountsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>List managed accounts request max results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List managed accounts request next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedAccountsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListManagedAccountsRequest:
    out: ListManagedAccountsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
