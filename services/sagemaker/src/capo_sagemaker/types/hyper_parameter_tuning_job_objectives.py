"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobObjectives``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective

HyperParameterTuningJobObjectives: TypeAlias = list[
    "capo_sagemaker.types.hyper_parameter_tuning_job_objective.HyperParameterTuningJobObjective"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobObjectives) -> list:
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.hyper_parameter_tuning_job_objective.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterTuningJobObjectives:
    import capo_sagemaker.types.hyper_parameter_tuning_job_objective

    out: HyperParameterTuningJobObjectives = []
    for item in data:
        out.append(
            capo_sagemaker.types.hyper_parameter_tuning_job_objective.deserialize_aws_json_1_1(
                item
            )
        )
    return out
