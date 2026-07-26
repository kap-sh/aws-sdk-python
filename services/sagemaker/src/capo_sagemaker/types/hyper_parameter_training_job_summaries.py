"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTrainingJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_training_job_summary

HyperParameterTrainingJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.hyper_parameter_training_job_summary.HyperParameterTrainingJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTrainingJobSummaries) -> list:
    import capo_sagemaker.types.hyper_parameter_training_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.hyper_parameter_training_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterTrainingJobSummaries:
    import capo_sagemaker.types.hyper_parameter_training_job_summary

    out: HyperParameterTrainingJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.hyper_parameter_training_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
