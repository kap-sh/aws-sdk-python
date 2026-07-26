"""Generated from Smithy shape ``com.amazonaws.sesv2#ListContactListsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.max_items
    import capo_sesv2.types.next_token


class ListContactListsRequest(TypedDict, closed=True):
    page_size: NotRequired["capo_sesv2.types.max_items.MaxItems"]
    """<p>Maximum number of contact lists to return at once. Use this parameter to paginate results. If additional contact lists exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional lists.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional contact lists available to be listed. Use the token provided in the Response to use in the subsequent call to ListContactLists with the same parameters to retrieve the next page of contact lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactListsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContactListsRequest:
    out: ListContactListsRequest = {}  # type: ignore[typeddict-item]
    return out
