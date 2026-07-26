"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_summary

HyperParameterTuningJobSummaries: TypeAlias = list[
    "capo_sagemaker.types.hyper_parameter_tuning_job_summary.HyperParameterTuningJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobSummaries) -> list:
    import capo_sagemaker.types.hyper_parameter_tuning_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.hyper_parameter_tuning_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterTuningJobSummaries:
    import capo_sagemaker.types.hyper_parameter_tuning_job_summary

    out: HyperParameterTuningJobSummaries = []
    for item in data:
        out.append(
            capo_sagemaker.types.hyper_parameter_tuning_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
