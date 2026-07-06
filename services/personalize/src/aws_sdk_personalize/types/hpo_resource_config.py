"""Generated from Smithy shape ``com.amazonaws.personalize#HPOResourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.hpo_resource


class HPOResourceConfig(TypedDict, closed=True):
    max_number_of_training_jobs: NotRequired[
        "aws_sdk_personalize.types.hpo_resource.HPOResource"
    ]
    """<p>The maximum number of training jobs when you create a solution version. The maximum value for <code>maxNumberOfTrainingJobs</code> is <code>40</code>.</p>"""
    max_parallel_training_jobs: NotRequired[
        "aws_sdk_personalize.types.hpo_resource.HPOResource"
    ]
    """<p>The maximum number of parallel training jobs when you create a solution version. The maximum value for <code>maxParallelTrainingJobs</code> is <code>10</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HPOResourceConfig) -> dict:
    out: dict = {}
    if "max_number_of_training_jobs" in value:
        out["maxNumberOfTrainingJobs"] = value["max_number_of_training_jobs"]
    if "max_parallel_training_jobs" in value:
        out["maxParallelTrainingJobs"] = value["max_parallel_training_jobs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HPOResourceConfig:
    out: HPOResourceConfig = {}  # type: ignore[typeddict-item]
    if "maxNumberOfTrainingJobs" in data:
        out["max_number_of_training_jobs"] = data["maxNumberOfTrainingJobs"]
    if "maxParallelTrainingJobs" in data:
        out["max_parallel_training_jobs"] = data["maxParallelTrainingJobs"]
    return out
