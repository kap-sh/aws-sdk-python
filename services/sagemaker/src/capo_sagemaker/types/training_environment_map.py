"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingEnvironmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_environment_key
    import capo_sagemaker.types.training_environment_value

TrainingEnvironmentMap: TypeAlias = dict[
    "capo_sagemaker.types.training_environment_key.TrainingEnvironmentKey",
    "capo_sagemaker.types.training_environment_value.TrainingEnvironmentValue",
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
