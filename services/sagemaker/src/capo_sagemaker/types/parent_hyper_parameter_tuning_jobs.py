"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParentHyperParameterTuningJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.parent_hyper_parameter_tuning_job

ParentHyperParameterTuningJobs: TypeAlias = list[
    "capo_sagemaker.types.parent_hyper_parameter_tuning_job.ParentHyperParameterTuningJob"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParentHyperParameterTuningJobs) -> list:
    import capo_sagemaker.types.parent_hyper_parameter_tuning_job

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.parent_hyper_parameter_tuning_job.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ParentHyperParameterTuningJobs:
    import capo_sagemaker.types.parent_hyper_parameter_tuning_job

    out: ParentHyperParameterTuningJobs = []
    for item in data:
        out.append(
            capo_sagemaker.types.parent_hyper_parameter_tuning_job.deserialize_aws_json_1_1(
                item
            )
        )
    return out
