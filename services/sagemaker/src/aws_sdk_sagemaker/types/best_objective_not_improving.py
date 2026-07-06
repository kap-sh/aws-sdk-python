"""Generated from Smithy shape ``com.amazonaws.sagemaker#BestObjectiveNotImproving``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_number_of_training_jobs_not_improving


class BestObjectiveNotImproving(TypedDict, closed=True):
    max_number_of_training_jobs_not_improving: NotRequired[
        "aws_sdk_sagemaker.types.max_number_of_training_jobs_not_improving.MaxNumberOfTrainingJobsNotImproving"
    ]
    """<p>The number of training jobs that have failed to improve model performance by 1% or greater over prior training jobs as evaluated against an objective function.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BestObjectiveNotImproving) -> dict:
    out: dict = {}
    if "max_number_of_training_jobs_not_improving" in value:
        out["MaxNumberOfTrainingJobsNotImproving"] = value[
            "max_number_of_training_jobs_not_improving"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> BestObjectiveNotImproving:
    out: BestObjectiveNotImproving = {}  # type: ignore[typeddict-item]
    if "MaxNumberOfTrainingJobsNotImproving" in data:
        out["max_number_of_training_jobs_not_improving"] = data[
            "MaxNumberOfTrainingJobsNotImproving"
        ]
    return out
