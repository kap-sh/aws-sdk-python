"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTrainingJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_job_arn


class CreateTrainingJobResponse(TypedDict):
    training_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTrainingJobResponse) -> dict:
    out: dict = {}
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTrainingJobResponse:
    out: CreateTrainingJobResponse = {}  # type: ignore[typeddict-item]
    if "TrainingJobArn" in data:
        out["training_job_arn"] = data["TrainingJobArn"]
    return out
