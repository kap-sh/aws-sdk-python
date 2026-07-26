"""Generated from Smithy shape ``com.amazonaws.bedrock#ListEvaluationJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.application_type
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_job_status
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.timestamp


class ListEvaluationJobsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>A filter to only list evaluation jobs created after a specified time.</p>"""
    creation_time_before: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>A filter to only list evaluation jobs created before a specified time.</p>"""
    status_equals: NotRequired[
        "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
    ]
    """<p>A filter to only list evaluation jobs that are of a certain status.</p>"""
    application_type_equals: NotRequired[
        "capo_bedrock.types.application_type.ApplicationType"
    ]
    """<p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>"""
    name_contains: NotRequired[
        "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
    ]
    """<p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>"""
    sort_by: NotRequired["capo_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>"""
    sort_order: NotRequired["capo_bedrock.types.sort_order.SortOrder"]
    """<p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluationJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEvaluationJobsRequest:
    out: ListEvaluationJobsRequest = {}  # type: ignore[typeddict-item]
    return out
