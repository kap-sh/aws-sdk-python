"""Generated from Smithy shape ``com.amazonaws.datasync#Ec2SecurityGroupArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_security_group_arn

Ec2SecurityGroupArnList: TypeAlias = list[
    "aws_sdk_datasync.types.ec2_security_group_arn.Ec2SecurityGroupArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2SecurityGroupArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Ec2SecurityGroupArnList:
    return list(data)
