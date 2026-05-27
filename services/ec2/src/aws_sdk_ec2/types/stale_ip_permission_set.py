"""Generated from Smithy shape ``com.amazonaws.ec2#StaleIpPermissionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_ip_permission

StaleIpPermissionSet: TypeAlias = list[
    "aws_sdk_ec2.types.stale_ip_permission.StaleIpPermission"
]
