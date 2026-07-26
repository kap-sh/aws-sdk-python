"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_execution_arn


class DescribePipelineExecutionRequest(TypedDict, closed=True):
    pipeline_execution_arn: NotRequired[
        "capo_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the pipeline execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineExecutionRequest) -> dict:
    out: dict = {}
    if "pipeline_execution_arn" in value:
        out["PipelineExecutionArn"] = value["pipeline_execution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineExecutionRequest:
    out: DescribePipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    if "PipelineExecutionArn" in data:
        out["pipeline_execution_arn"] = data["PipelineExecutionArn"]
    return out
