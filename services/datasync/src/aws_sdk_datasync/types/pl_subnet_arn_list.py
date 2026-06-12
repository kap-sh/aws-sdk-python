"""Generated from Smithy shape ``com.amazonaws.datasync#PLSubnetArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.ec2_subnet_arn

PLSubnetArnList: TypeAlias = list["aws_sdk_datasync.types.ec2_subnet_arn.Ec2SubnetArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PLSubnetArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PLSubnetArnList:
    return list(data)
