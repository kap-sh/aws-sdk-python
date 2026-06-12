"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingEnvironmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_environment_key
    import aws_sdk_sagemaker.types.training_environment_value

TrainingEnvironmentMap: TypeAlias = dict[
    "aws_sdk_sagemaker.types.training_environment_key.TrainingEnvironmentKey",
    "aws_sdk_sagemaker.types.training_environment_value.TrainingEnvironmentValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TrainingEnvironmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingEnvironmentMap:
    out: TrainingEnvironmentMap = {}
    for key, value in data.items():
        out[key] = value
    return out
