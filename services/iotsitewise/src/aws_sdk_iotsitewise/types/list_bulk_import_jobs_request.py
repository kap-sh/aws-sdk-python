"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListBulkImportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.list_bulk_import_jobs_filter
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.next_token


class ListBulkImportJobsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results to return for each paginated request.</p>"""
    filter: NotRequired[
        "aws_sdk_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
    ]
    """<p>You can use a filter to select the bulk import jobs that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBulkImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBulkImportJobsRequest:
    out: ListBulkImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
