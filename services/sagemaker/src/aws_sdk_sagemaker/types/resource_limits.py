"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_max_runtime_in_seconds
    import aws_sdk_sagemaker.types.max_number_of_training_jobs
    import aws_sdk_sagemaker.types.max_parallel_training_jobs


class ResourceLimits(TypedDict, closed=True):
    max_number_of_training_jobs: NotRequired[
        "aws_sdk_sagemaker.types.max_number_of_training_jobs.MaxNumberOfTrainingJobs"
    ]
    """<p>The maximum number of training jobs that a hyperparameter tuning job can launch.</p>"""
    max_parallel_training_jobs: NotRequired[
        "aws_sdk_sagemaker.types.max_parallel_training_jobs.MaxParallelTrainingJobs"
    ]
    """<p>The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.</p>"""
    max_runtime_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_max_runtime_in_seconds.HyperParameterTuningMaxRuntimeInSeconds"
    ]
    """<p>The maximum time in seconds that a hyperparameter tuning job can run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceLimits) -> dict:
    out: dict = {}
    if "max_number_of_training_jobs" in value:
        out["MaxNumberOfTrainingJobs"] = value["max_number_of_training_jobs"]
    if "max_parallel_training_jobs" in value:
        out["MaxParallelTrainingJobs"] = value["max_parallel_training_jobs"]
    if "max_runtime_in_seconds" in value:
        out["MaxRuntimeInSeconds"] = value["max_runtime_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceLimits:
    out: ResourceLimits = {}  # type: ignore[typeddict-item]
    if "MaxNumberOfTrainingJobs" in data:
        out["max_number_of_training_jobs"] = data["MaxNumberOfTrainingJobs"]
    if "MaxParallelTrainingJobs" in data:
        out["max_parallel_training_jobs"] = data["MaxParallelTrainingJobs"]
    if "MaxRuntimeInSeconds" in data:
        out["max_runtime_in_seconds"] = data["MaxRuntimeInSeconds"]
    return out
