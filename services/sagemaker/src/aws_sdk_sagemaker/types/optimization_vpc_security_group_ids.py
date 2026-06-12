"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationVpcSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_vpc_security_group_id

OptimizationVpcSecurityGroupIds: TypeAlias = list[
    "aws_sdk_sagemaker.types.optimization_vpc_security_group_id.OptimizationVpcSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationVpcSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OptimizationVpcSecurityGroupIds:
    return list(data)
