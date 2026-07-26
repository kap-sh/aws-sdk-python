"""Generated from Smithy shape ``com.amazonaws.bedrock#ListProvisionedModelThroughputsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.provisioned_model_name
    import capo_bedrock.types.provisioned_model_status
    import capo_bedrock.types.sort_by_provisioned_models
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.timestamp


class ListProvisionedModelThroughputsRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>A filter that returns Provisioned Throughputs created after the specified time. </p>"""
    creation_time_before: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>A filter that returns Provisioned Throughputs created before the specified time. </p>"""
    status_equals: NotRequired[
        "capo_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
    ]
    """<p>A filter that returns Provisioned Throughputs if their statuses matches the value that you specify.</p>"""
    model_arn_equals: NotRequired["capo_bedrock.types.model_arn.ModelArn"]
    """<p>A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify.</p>"""
    name_contains: NotRequired[
        "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
    ]
    """<p>A filter that returns Provisioned Throughputs if their name contains the expression that you specify.</p>"""
    max_results: NotRequired["capo_bedrock.types.max_results.MaxResults"]
    """<p>THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another list request.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there are more results than the number you specified in the <code>maxResults</code> field, the response returns a <code>nextToken</code> value. To see the next batch of results, specify the <code>nextToken</code> value in this field.</p>"""
    sort_by: NotRequired[
        "capo_bedrock.types.sort_by_provisioned_models.SortByProvisionedModels"
    ]
    """<p>The field by which to sort the returned list of Provisioned Throughputs.</p>"""
    sort_order: NotRequired["capo_bedrock.types.sort_order.SortOrder"]
    """<p>The sort order of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProvisionedModelThroughputsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProvisionedModelThroughputsRequest:
    out: ListProvisionedModelThroughputsRequest = {}  # type: ignore[typeddict-item]
    return out
