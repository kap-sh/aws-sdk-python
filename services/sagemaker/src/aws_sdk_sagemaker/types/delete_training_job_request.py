"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteTrainingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_job_name


class DeleteTrainingJobRequest(TypedDict):
    training_job_name: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrainingJobRequest) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrainingJobRequest:
    out: DeleteTrainingJobRequest = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
    return out
