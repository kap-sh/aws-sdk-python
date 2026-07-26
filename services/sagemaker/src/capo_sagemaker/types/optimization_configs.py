"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.optimization_config

OptimizationConfigs: TypeAlias = list[
    "capo_sagemaker.types.optimization_config.OptimizationConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationConfigs) -> list:
    import capo_sagemaker.types.optimization_config

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.optimization_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OptimizationConfigs:
    import capo_sagemaker.types.optimization_config

    out: OptimizationConfigs = []
    for item in data:
        out.append(
            capo_sagemaker.types.optimization_config.deserialize_aws_json_1_1(item)
        )
    return out
