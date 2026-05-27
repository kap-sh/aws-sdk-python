"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission

LoadPermissionList: TypeAlias = list["aws_sdk_ec2.types.load_permission.LoadPermission"]
