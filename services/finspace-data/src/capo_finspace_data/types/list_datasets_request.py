"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListDatasetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.result_limit


class ListDatasetsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: NotRequired["capo_finspace_data.types.result_limit.ResultLimit"]
    """<p>The maximum number of results per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDatasetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDatasetsRequest:
    out: ListDatasetsRequest = {}  # type: ignore[typeddict-item]
    return out
