"""Generated from Smithy shape ``com.amazonaws.backup#ListLegalHoldsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.max_results
    import capo_backup.types.string


class ListLegalHoldsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    max_results: NotRequired["capo_backup.types.max_results.MaxResults"]
    """<p>The maximum number of resource list items to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLegalHoldsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLegalHoldsInput:
    out: ListLegalHoldsInput = {}  # type: ignore[typeddict-item]
    return out
