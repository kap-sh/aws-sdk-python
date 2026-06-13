"""Generated from Smithy shape ``com.amazonaws.bedrock#ListCustomModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.custom_model_name
    import aws_sdk_bedrock.types.foundation_model_arn
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.model_arn
    import aws_sdk_bedrock.types.model_status
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_models_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.timestamp


class ListCustomModelsRequest(TypedDict):
    creation_time_before: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return custom models created before the specified time. </p>"""
    creation_time_after: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return custom models created after the specified time. </p>"""
    name_contains: NotRequired[
        "aws_sdk_bedrock.types.custom_model_name.CustomModelName"
    ]
    """<p>Return custom models only if the job name contains these characters.</p>"""
    base_model_arn_equals: NotRequired["aws_sdk_bedrock.types.model_arn.ModelArn"]
    """<p>Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter.</p>"""
    foundation_model_arn_equals: NotRequired[
        "aws_sdk_bedrock.types.foundation_model_arn.FoundationModelArn"
    ]
    """<p>Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter.</p>"""
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    sort_by: NotRequired["aws_sdk_bedrock.types.sort_models_by.SortModelsBy"]
    """<p>The field to sort by in the returned list of models.</p>"""
    sort_order: NotRequired["aws_sdk_bedrock.types.sort_order.SortOrder"]
    """<p>The sort order of the results.</p>"""
    is_owned: NotRequired["bool"]
    """<p>Return custom models depending on if the current account owns them (<code>true</code>) or if they were shared with the current account (<code>false</code>).</p>"""
    model_status: NotRequired["aws_sdk_bedrock.types.model_status.ModelStatus"]
    """<p>The status of them model to filter results by. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - Include only models that are currently being created and validated.</p> </li> <li> <p> <code>Active</code> - Include only models that have been successfully created and are ready for use.</p> </li> <li> <p> <code>Failed</code> - Include only models where the creation process failed.</p> </li> </ul> <p>If you don't specify a status, the API returns models in all states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCustomModelsRequest:
    out: ListCustomModelsRequest = {}  # type: ignore[typeddict-item]
    return out
