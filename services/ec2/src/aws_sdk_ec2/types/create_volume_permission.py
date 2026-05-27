"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class CreateVolumePermission(TypedDict):
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account to be added or removed.</p>"""
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The group to be added or removed. The possible value is <code>all</code>.</p>"""
