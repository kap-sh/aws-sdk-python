"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTopologyInstanceIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_id

DescribeInstanceTopologyInstanceIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.instance_id.InstanceId"
]
