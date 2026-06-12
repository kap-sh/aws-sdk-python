"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationVpcSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_vpc_subnet_id

OptimizationVpcSubnets: TypeAlias = list[
    "aws_sdk_sagemaker.types.optimization_vpc_subnet_id.OptimizationVpcSubnetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationVpcSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OptimizationVpcSubnets:
    return list(data)
