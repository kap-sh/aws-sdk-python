"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_config

OptimizationConfigs: TypeAlias = list[
    "aws_sdk_sagemaker.types.optimization_config.OptimizationConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationConfigs) -> list:
    import aws_sdk_sagemaker.types.optimization_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.optimization_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OptimizationConfigs:
    import aws_sdk_sagemaker.types.optimization_config

    out: OptimizationConfigs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.optimization_config.deserialize_aws_json_1_1(item)
        )
    return out
