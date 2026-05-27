"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_permission

LaunchPermissionList: TypeAlias = list[
    "aws_sdk_ec2.types.launch_permission.LaunchPermission"
]
