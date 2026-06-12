"""Generated from Smithy shape ``com.amazonaws.sagemaker#NeoVpcSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.neo_vpc_security_group_id

NeoVpcSecurityGroupIds: TypeAlias = list[
    "aws_sdk_sagemaker.types.neo_vpc_security_group_id.NeoVpcSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeoVpcSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NeoVpcSecurityGroupIds:
    return list(data)
