"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.pipeline_name_or_arn
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListPipelineVersionsRequest(TypedDict, closed=True):
    pipeline_name: NotRequired[
        "capo_sagemaker.types.pipeline_name_or_arn.PipelineNameOrArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipeline versions that were created after a specified time.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipeline versions that were created before a specified time.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for the results.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineVersions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipeline versions, use this token in your next request.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of pipeline versions to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineVersionsRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineVersionsRequest:
    out: ListPipelineVersionsRequest = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "CreatedAfter" in data:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if "CreatedBefore" in data:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
