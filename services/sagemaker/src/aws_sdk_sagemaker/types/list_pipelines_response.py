"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelinesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.pipeline_summary_list


class ListPipelinesResponse(TypedDict, closed=True):
    pipeline_summaries: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_summary_list.PipelineSummaryList"
    ]
    """<p>Contains a sorted list of <code>PipelineSummary</code> objects matching the specified filters. Each <code>PipelineSummary</code> consists of PipelineArn, PipelineName, ExperimentName, PipelineDescription, CreationTime, LastModifiedTime, LastRunTime, and RoleArn. This list can be empty. </p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelines</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipelines, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelinesResponse) -> dict:
    out: dict = {}
    if "pipeline_summaries" in value:
        import aws_sdk_sagemaker.types.pipeline_summary_list

        out["PipelineSummaries"] = (
            aws_sdk_sagemaker.types.pipeline_summary_list.serialize_aws_json_1_1(
                value["pipeline_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelinesResponse:
    out: ListPipelinesResponse = {}  # type: ignore[typeddict-item]
    if "PipelineSummaries" in data:
        import aws_sdk_sagemaker.types.pipeline_summary_list

        out["pipeline_summaries"] = (
            aws_sdk_sagemaker.types.pipeline_summary_list.deserialize_aws_json_1_1(
                data["PipelineSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
