"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteHyperParameterTuningJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name


class DeleteHyperParameterTuningJobRequest(TypedDict):
    hyper_parameter_tuning_job_name: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the hyperparameter tuning job that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHyperParameterTuningJobRequest) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHyperParameterTuningJobRequest:
    out: DeleteHyperParameterTuningJobRequest = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobName" in data:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    return out
