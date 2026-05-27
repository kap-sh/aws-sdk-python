"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class LaunchPermission(TypedDict):
    organization_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an organization.</p>"""
    organizational_unit_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of an organizational unit (OU).</p>"""
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p> <p>Constraints: Up to 10 000 account IDs can be specified in a single request.</p>"""
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The name of the group.</p>"""
