"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTrainingJobDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_training_job_definition

HyperParameterTrainingJobDefinitions: TypeAlias = list[
    "capo_sagemaker.types.hyper_parameter_training_job_definition.HyperParameterTrainingJobDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTrainingJobDefinitions) -> list:
    import capo_sagemaker.types.hyper_parameter_training_job_definition

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.hyper_parameter_training_job_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterTrainingJobDefinitions:
    import capo_sagemaker.types.hyper_parameter_training_job_definition

    out: HyperParameterTrainingJobDefinitions = []
    for item in data:
        out.append(
            capo_sagemaker.types.hyper_parameter_training_job_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
