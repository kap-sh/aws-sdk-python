"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission

NetworkInterfacePermissionList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_permission.NetworkInterfacePermission"
]
