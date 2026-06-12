"""Generated from Smithy shape ``com.amazonaws.bedrock#ListAdvancedPromptOptimizationJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_jobs_by
    import aws_sdk_bedrock.types.sort_order


class ListAdvancedPromptOptimizationJobsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>"""
    sort_by: NotRequired["aws_sdk_bedrock.types.sort_jobs_by.SortJobsBy"]
    """<p>The field to sort the results by.</p>"""
    sort_order: NotRequired["aws_sdk_bedrock.types.sort_order.SortOrder"]
    """<p>The sort order for the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAdvancedPromptOptimizationJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAdvancedPromptOptimizationJobsRequest:
    out: ListAdvancedPromptOptimizationJobsRequest = {}  # type: ignore[typeddict-item]
    return out
