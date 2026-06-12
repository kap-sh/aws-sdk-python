"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_type

OptimizationTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.optimization_type.OptimizationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OptimizationTypes:
    return list(data)
