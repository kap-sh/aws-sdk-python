"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelCopyJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.account_id
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.model_copy_job_status
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.timestamp


class ListModelCopyJobsRequest(TypedDict):
    creation_time_after: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Filters for model copy jobs created after the specified time.</p>"""
    creation_time_before: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Filters for model copy jobs created before the specified time. </p>"""
    status_equals: NotRequired[
        "aws_sdk_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
    ]
    """<p>Filters for model copy jobs whose status matches the value that you specify.</p>"""
    source_account_equals: NotRequired["aws_sdk_bedrock.types.account_id.AccountId"]
    """<p>Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify.</p>"""
    source_model_arn_equals: NotRequired["aws_sdk_bedrock.types.model_arn.ModelArn"]
    """<p>Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify.</p>"""
    target_model_name_contains: NotRequired[
        "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>Filters for model copy jobs in which the name of the copied model contains the string that you specify.</p>"""
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    sort_by: NotRequired["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>The field to sort by in the returned list of model copy jobs.</p>"""
    sort_order: NotRequired["aws_sdk_bedrock.types.sort_order.SortOrder"]
    """<p>Specifies whether to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelCopyJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelCopyJobsRequest:
    out: ListModelCopyJobsRequest = {}  # type: ignore[typeddict-item]
    return out
