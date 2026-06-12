"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHyperParameterTuningJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn


class CreateHyperParameterTuningJobResponse(TypedDict):
    hyper_parameter_tuning_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_arn.HyperParameterTuningJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the tuning job. SageMaker assigns an ARN to a hyperparameter tuning job when you create it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHyperParameterTuningJobResponse) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_arn" in value:
        out["HyperParameterTuningJobArn"] = value["hyper_parameter_tuning_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHyperParameterTuningJobResponse:
    out: CreateHyperParameterTuningJobResponse = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobArn" in data:
        out["hyper_parameter_tuning_job_arn"] = data["HyperParameterTuningJobArn"]
    return out
