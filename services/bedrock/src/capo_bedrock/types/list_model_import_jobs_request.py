"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.job_name
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_import_job_status
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.timestamp


class ListModelImportJobsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Return import jobs that were created after the specified time.</p>"""
    creation_time_before: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Return import jobs that were created before the specified time.</p>"""
    status_equals: NotRequired[
        "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
    ]
    """<p>Return imported jobs with the specified status.</p>"""
    name_contains: NotRequired["capo_bedrock.types.job_name.JobName"]
    """<p>Return imported jobs only if the job name contains these characters.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    sort_by: NotRequired["capo_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>The field to sort by in the returned list of imported jobs.</p>"""
    sort_order: NotRequired["capo_bedrock.types.sort_order.SortOrder"]
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelImportJobsRequest:
    out: ListModelImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
