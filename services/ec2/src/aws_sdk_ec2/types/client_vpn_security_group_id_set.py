"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnSecurityGroupIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_id

ClientVpnSecurityGroupIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
]
