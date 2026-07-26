"""Generated from Smithy shape ``com.amazonaws.macie2#ListAllowListsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.max_results


class ListAllowListsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_macie2.types.max_results.MaxResults"]
    """<p>The maximum number of items to include in each page of a paginated response.</p>"""
    next_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The nextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAllowListsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAllowListsRequest:
    out: ListAllowListsRequest = {}  # type: ignore[typeddict-item]
    return out
