"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_job_summary

TrainingJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.training_job_summary.TrainingJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobSummaries) -> list:
    import capo_sagemaker.types.training_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingJobSummaries:
    import capo_sagemaker.types.training_job_summary

    out: TrainingJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_job_summary.deserialize_aws_json_1_1(item)
        )
    return out
