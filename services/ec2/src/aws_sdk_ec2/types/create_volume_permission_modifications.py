"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermissionModifications``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_volume_permission_list


class CreateVolumePermissionModifications(TypedDict):
    add: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Adds the specified Amazon Web Services account ID or group to the list.</p>"""
    remove: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>Removes the specified Amazon Web Services account ID or group from the list.</p>"""
