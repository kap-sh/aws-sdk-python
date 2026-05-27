"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesSecurityGroupIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_id

ScheduledInstancesSecurityGroupIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
]
