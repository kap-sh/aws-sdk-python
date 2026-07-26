"""Generated from Smithy shape ``com.amazonaws.finspacedata#ListDataViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.pagination_token
    import capo_finspace_data.types.result_limit


class ListDataViewsRequest(TypedDict, closed=True):
    dataset_id: "capo_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier of the Dataset for which to retrieve Dataviews.</p>"""
    next_token: NotRequired["capo_finspace_data.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: NotRequired["capo_finspace_data.types.result_limit.ResultLimit"]
    """<p>The maximum number of results per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataViewsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataViewsRequest:
    out: ListDataViewsRequest = {}  # type: ignore[typeddict-item]
    return out
