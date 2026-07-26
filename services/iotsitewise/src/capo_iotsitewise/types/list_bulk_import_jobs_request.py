"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListBulkImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.list_bulk_import_jobs_filter
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.next_token


class ListBulkImportJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["capo_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    filter: NotRequired[
        "capo_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
    ]
    """<p>You can use a filter to select the bulk import jobs that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBulkImportJobsRequest:
    out: ListBulkImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
