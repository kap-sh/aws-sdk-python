"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrainingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_job_arn


class UpdateTrainingJobResponse(TypedDict, closed=True):
    training_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrainingJobResponse) -> dict:
    out: dict = {}
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrainingJobResponse:
    out: UpdateTrainingJobResponse = {}  # type: ignore[typeddict-item]
    if "TrainingJobArn" in data:
        out["training_job_arn"] = data["TrainingJobArn"]
    return out
