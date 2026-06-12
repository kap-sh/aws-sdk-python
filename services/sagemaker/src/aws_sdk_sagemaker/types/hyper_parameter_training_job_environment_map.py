"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTrainingJobEnvironmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_environment_key
    import aws_sdk_sagemaker.types.hyper_parameter_training_job_environment_value

HyperParameterTrainingJobEnvironmentMap: TypeAlias = dict[
    "aws_sdk_sagemaker.types.hyper_parameter_training_job_environment_key.HyperParameterTrainingJobEnvironmentKey",
    "aws_sdk_sagemaker.types.hyper_parameter_training_job_environment_value.HyperParameterTrainingJobEnvironmentValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: HyperParameterTrainingJobEnvironmentMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTrainingJobEnvironmentMap:
    out: HyperParameterTrainingJobEnvironmentMap = {}
    for key, value in data.items():
        out[key] = value
    return out
