"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelinesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.pipeline_name
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.sort_pipelines_by
    import aws_sdk_sagemaker.types.timestamp


class ListPipelinesRequest(TypedDict):
    pipeline_name_prefix: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The prefix of the pipeline name.</p>"""
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipelines that were created after a specified time.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns the pipelines that were created before a specified time.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.sort_pipelines_by.SortPipelinesBy"]
    """<p>The field by which to sort results. The default is <code>CreatedTime</code>.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelines</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipelines, use the token in the next request.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of pipelines to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesRequest) -> dict:
    out: dict = {}
    if "pipeline_name_prefix" in value:
        out["PipelineNamePrefix"] = value["pipeline_name_prefix"]
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_pipelines_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_pipelines_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesRequest:
    out: ListPipelinesRequest = {}  # type: ignore[typeddict-item]
    if "PipelineNamePrefix" in data:
        out["pipeline_name_prefix"] = data["PipelineNamePrefix"]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_pipelines_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_pipelines_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
