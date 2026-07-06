"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopHyperParameterTuningJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name


class StopHyperParameterTuningJobRequest(TypedDict, closed=True):
    hyper_parameter_tuning_job_name: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_name.HyperParameterTuningJobName"
    ]
    """<p>The name of the tuning job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopHyperParameterTuningJobRequest) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_name" in value:
        out["HyperParameterTuningJobName"] = value["hyper_parameter_tuning_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopHyperParameterTuningJobRequest:
    out: StopHyperParameterTuningJobRequest = {}  # type: ignore[typeddict-item]
    if "HyperParameterTuningJobName" in data:
        out["hyper_parameter_tuning_job_name"] = data["HyperParameterTuningJobName"]
    return out
