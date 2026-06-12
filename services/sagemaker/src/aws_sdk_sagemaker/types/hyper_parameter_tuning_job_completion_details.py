"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobCompletionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.timestamp


class HyperParameterTuningJobCompletionDetails(TypedDict):
    number_of_training_jobs_objective_not_improving: NotRequired[
        "aws_sdk_sagemaker.types.integer.Integer"
    ]
    """<p>The number of training jobs launched by a tuning job that are not improving (1% or less) as measured by model performance evaluated against an objective function.</p>"""
    convergence_detected_time: NotRequired[
        "aws_sdk_sagemaker.types.timestamp.Timestamp"
    ]
    """<p>The time in timestamp format that AMT detected model convergence, as defined by a lack of significant improvement over time based on criteria developed over a wide range of diverse benchmarking tests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobCompletionDetails) -> dict:
    out: dict = {}
    if "number_of_training_jobs_objective_not_improving" in value:
        out["NumberOfTrainingJobsObjectiveNotImproving"] = value[
            "number_of_training_jobs_objective_not_improving"
        ]
    if "convergence_detected_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["ConvergenceDetectedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["convergence_detected_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobCompletionDetails:
    out: HyperParameterTuningJobCompletionDetails = {}  # type: ignore[typeddict-item]
    if "NumberOfTrainingJobsObjectiveNotImproving" in data:
        out["number_of_training_jobs_objective_not_improving"] = data[
            "NumberOfTrainingJobsObjectiveNotImproving"
        ]
    if "ConvergenceDetectedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["convergence_detected_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ConvergenceDetectedTime"]
            )
        )
    return out
