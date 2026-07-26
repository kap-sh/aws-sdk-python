"""Generated from Smithy shape ``com.amazonaws.lambda#ListCodeSigningConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.max_list_items
    import capo_lambda.types.string


class ListCodeSigningConfigsRequest(TypedDict, closed=True):
    marker: NotRequired["capo_lambda.types.string.String"]
    """<p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_lambda.types.max_list_items.MaxListItems"]
    """<p>Maximum number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSigningConfigsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeSigningConfigsRequest:
    out: ListCodeSigningConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
