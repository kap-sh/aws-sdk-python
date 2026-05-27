"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission_request

LoadPermissionListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.load_permission_request.LoadPermissionRequest"
]
