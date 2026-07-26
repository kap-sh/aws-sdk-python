"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTrainingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.training_job_name


class DescribeTrainingJobRequest(TypedDict, closed=True):
    training_job_name: NotRequired[
        "capo_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrainingJobRequest) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrainingJobRequest:
    out: DescribeTrainingJobRequest = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
    return out
