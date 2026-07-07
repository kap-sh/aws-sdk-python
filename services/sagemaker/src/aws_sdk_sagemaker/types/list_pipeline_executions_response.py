"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineExecutionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.pipeline_execution_summary_list


class ListPipelineExecutionsResponse(TypedDict, closed=True):
    pipeline_execution_summaries: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_summary_list.PipelineExecutionSummaryList"
    ]
    """<p>Contains a sorted list of pipeline execution summary objects matching the specified filters. Each run summary includes the Amazon Resource Name (ARN) of the pipeline execution, the run date, and the status. This list can be empty. </p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineExecutions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipeline executions, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionsResponse) -> dict:
    out: dict = {}
    if "pipeline_execution_summaries" in value:
        import aws_sdk_sagemaker.types.pipeline_execution_summary_list

        out["PipelineExecutionSummaries"] = (
            aws_sdk_sagemaker.types.pipeline_execution_summary_list.serialize_aws_json_1_1(
                value["pipeline_execution_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionsResponse:
    out: ListPipelineExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionSummaries" in data:
        import aws_sdk_sagemaker.types.pipeline_execution_summary_list

        out["pipeline_execution_summaries"] = (
            aws_sdk_sagemaker.types.pipeline_execution_summary_list.deserialize_aws_json_1_1(
                data["PipelineExecutionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
