"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_volume_permission

CreateVolumePermissionList: TypeAlias = list[
    "aws_sdk_ec2.types.create_volume_permission.CreateVolumePermission"
]
