"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelCustomizationJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.fine_tuning_job_status
    import aws_sdk_bedrock.types.job_name
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.timestamp


class ListModelCustomizationJobsRequest(TypedDict):
    creation_time_after: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return customization jobs created after the specified time. </p>"""
    creation_time_before: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return customization jobs created before the specified time. </p>"""
    status_equals: NotRequired[
        "aws_sdk_bedrock.types.fine_tuning_job_status.FineTuningJobStatus"
    ]
    """<p>Return customization jobs with the specified status. </p>"""
    name_contains: NotRequired["aws_sdk_bedrock.types.job_name.JobName"]
    """<p>Return customization jobs only if the job name contains these characters.</p>"""
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    sort_by: NotRequired["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>The field to sort by in the returned list of jobs.</p>"""
    sort_order: NotRequired["aws_sdk_bedrock.types.sort_order.SortOrder"]
    """<p>The sort order of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelCustomizationJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelCustomizationJobsRequest:
    out: ListModelCustomizationJobsRequest = {}  # type: ignore[typeddict-item]
    return out
