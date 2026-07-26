"""Generated from Smithy shape ``com.amazonaws.qapps#ListLibraryItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.page_limit
    import capo_qapps.types.pagination_token
    import capo_qapps.types.uuid


class ListLibraryItemsInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    limit: NotRequired["capo_qapps.types.page_limit.PageLimit"]
    """<p>The maximum number of library items to return in the response.</p>"""
    next_token: NotRequired["capo_qapps.types.pagination_token.PaginationToken"]
    """<p>The token to request the next page of results.</p>"""
    category_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>Optional category to filter the library items by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLibraryItemsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLibraryItemsInput:
    out: ListLibraryItemsInput = {}  # type: ignore[typeddict-item]
    return out
