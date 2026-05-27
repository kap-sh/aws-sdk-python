"""Generated from Smithy shape ``com.amazonaws.ec2#IpPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_permission

IpPermissionList: TypeAlias = list["aws_sdk_ec2.types.ip_permission.IpPermission"]
