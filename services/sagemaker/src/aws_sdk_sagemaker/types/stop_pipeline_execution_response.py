"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopPipelineExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_execution_arn


class StopPipelineExecutionResponse(TypedDict, closed=True):
    pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopPipelineExecutionResponse) -> dict:
    out: dict = {}
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopPipelineExecutionResponse:
    out: StopPipelineExecutionResponse = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    return out
