"""Generated from Smithy shape ``com.amazonaws.bedrock#ListImportedModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.imported_model_name
    import aws_sdk_bedrock.types.max_results
    import aws_sdk_bedrock.types.pagination_token
    import aws_sdk_bedrock.types.sort_models_by
    import aws_sdk_bedrock.types.sort_order
    import aws_sdk_bedrock.types.timestamp


class ListImportedModelsRequest(TypedDict):
    creation_time_before: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return imported models that created before the specified time.</p>"""
    creation_time_after: NotRequired["aws_sdk_bedrock.types.timestamp.Timestamp"]
    """<p>Return imported models that were created after the specified time.</p>"""
    name_contains: NotRequired[
        "aws_sdk_bedrock.types.imported_model_name.ImportedModelName"
    ]
    """<p>Return imported models only if the model name contains these characters.</p>"""
    max_results: NotRequired["aws_sdk_bedrock.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    next_token: NotRequired["aws_sdk_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>"""
    sort_by: NotRequired["aws_sdk_bedrock.types.sort_models_by.SortModelsBy"]
    """<p>The field to sort by in the returned list of imported models.</p>"""
    sort_order: NotRequired["aws_sdk_bedrock.types.sort_order.SortOrder"]
    """<p>Specifies whetehr to sort the results in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportedModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListImportedModelsRequest:
    out: ListImportedModelsRequest = {}  # type: ignore[typeddict-item]
    return out
