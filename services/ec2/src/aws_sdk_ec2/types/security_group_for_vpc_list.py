"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupForVpcList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_for_vpc

SecurityGroupForVpcList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_for_vpc.SecurityGroupForVpc"
]
