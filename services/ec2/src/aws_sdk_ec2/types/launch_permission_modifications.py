"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchPermissionModifications``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_permission_list


class LaunchPermissionModifications(TypedDict):
    add: NotRequired["aws_sdk_ec2.types.launch_permission_list.LaunchPermissionList"]
    """<p>The Amazon Web Services account ID, organization ARN, or OU ARN to add to the list of launch permissions for the AMI.</p>"""
    remove: NotRequired["aws_sdk_ec2.types.launch_permission_list.LaunchPermissionList"]
    """<p>The Amazon Web Services account ID, organization ARN, or OU ARN to remove from the list of launch permissions for the AMI.</p>"""
