"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateOptimizationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_job_arn


class CreateOptimizationJobResponse(TypedDict):
    optimization_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_arn.OptimizationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOptimizationJobResponse) -> dict:
    out: dict = {}
    if "optimization_job_arn" in value:
        out["OptimizationJobArn"] = value["optimization_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOptimizationJobResponse:
    out: CreateOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if "OptimizationJobArn" in data:
        out["optimization_job_arn"] = data["OptimizationJobArn"]
    return out
