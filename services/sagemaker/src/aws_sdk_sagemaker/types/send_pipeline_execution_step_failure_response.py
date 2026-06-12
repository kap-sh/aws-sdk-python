"""Generated from Smithy shape ``com.amazonaws.sagemaker#SendPipelineExecutionStepFailureResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.pipeline_execution_arn


class SendPipelineExecutionStepFailureResponse(TypedDict):
    pipeline_execution_arn: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendPipelineExecutionStepFailureResponse) -> dict:
    out: dict = {}
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendPipelineExecutionStepFailureResponse:
    out: SendPipelineExecutionStepFailureResponse = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    return out
