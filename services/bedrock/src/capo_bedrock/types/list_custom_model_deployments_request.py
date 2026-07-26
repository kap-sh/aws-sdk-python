"""Generated from Smithy shape ``com.amazonaws.bedrock#ListCustomModelDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_models_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.timestamp


class ListCustomModelDeploymentsRequest(TypedDict, closed=True):
    created_before: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Filters deployments created before the specified date and time.</p>"""
    created_after: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Filters deployments created after the specified date and time.</p>"""
    name_contains: NotRequired[
        "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
    ]
    """<p>Filters deployments whose names contain the specified string. </p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>The token for the next set of results. Use this token to retrieve additional results when the response is truncated.</p>"""
    sort_by: NotRequired["capo_bedrock.types.sort_models_by.SortModelsBy"]
    """<p>The field to sort the results by. The only supported value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_bedrock.types.sort_order.SortOrder"]
    """<p>The sort order for the results. Valid values are <code>Ascending</code> and <code>Descending</code>. Default is <code>Descending</code>.</p>"""
    status_equals: NotRequired[
        "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
    ]
    """<p>Filters deployments by status. Valid values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>"""
    model_arn_equals: NotRequired["capo_bedrock.types.custom_model_arn.CustomModelArn"]
    """<p>Filters deployments by the Amazon Resource Name (ARN) of the associated custom model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomModelDeploymentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomModelDeploymentsRequest:
    out: ListCustomModelDeploymentsRequest = {}  # type: ignore[typeddict-item]
    return out
