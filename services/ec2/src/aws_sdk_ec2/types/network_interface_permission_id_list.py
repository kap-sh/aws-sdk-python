"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermissionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission_id

NetworkInterfacePermissionIdList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_permission_id.NetworkInterfacePermissionId"
]
