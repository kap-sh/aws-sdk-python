"""Generated from Smithy shape ``com.amazonaws.ec2#StaleSecurityGroupSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_security_group

StaleSecurityGroupSet: TypeAlias = list[
    "aws_sdk_ec2.types.stale_security_group.StaleSecurityGroup"
]
