"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class LoadPermission(TypedDict):
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The name of the group.</p>"""
