"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineExecutionStepsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.pipeline_execution_step_list


class ListPipelineExecutionStepsResponse(TypedDict, closed=True):
    pipeline_execution_steps: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_step_list.PipelineExecutionStepList"
    ]
    """<p>A list of <code>PipeLineExecutionStep</code> objects. Each <code>PipeLineExecutionStep</code> consists of StepName, StartTime, EndTime, StepStatus, and Metadata. Metadata is an object with properties for each job that contains relevant information about the job created by the step.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineExecutionSteps</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of pipeline execution steps, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionStepsResponse) -> dict:
    out: dict = {}
    if "pipeline_execution_steps" in value:
        import aws_sdk_sagemaker.types.pipeline_execution_step_list

        out["PipelineExecutionSteps"] = (
            aws_sdk_sagemaker.types.pipeline_execution_step_list.serialize_aws_json_1_1(
                value["pipeline_execution_steps"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionStepsResponse:
    out: ListPipelineExecutionStepsResponse = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionSteps" in data:
        import aws_sdk_sagemaker.types.pipeline_execution_step_list

        out["pipeline_execution_steps"] = (
            aws_sdk_sagemaker.types.pipeline_execution_step_list.deserialize_aws_json_1_1(
                data["PipelineExecutionSteps"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
