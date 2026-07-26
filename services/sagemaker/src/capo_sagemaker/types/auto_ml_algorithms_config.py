"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithmsConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_algorithm_config

AutoMLAlgorithmsConfig: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_algorithm_config.AutoMLAlgorithmConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLAlgorithmsConfig) -> list:
    import capo_sagemaker.types.auto_ml_algorithm_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.auto_ml_algorithm_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLAlgorithmsConfig:
    import capo_sagemaker.types.auto_ml_algorithm_config

    out: AutoMLAlgorithmsConfig = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_algorithm_config.deserialize_aws_json_1_1(item)
        )
    return out
