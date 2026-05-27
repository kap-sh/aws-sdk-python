"""Generated from Smithy shape ``com.amazonaws.ec2#StaleSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_ip_permission_set
    import aws_sdk_ec2.types.string


class StaleSecurityGroup(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the security group.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""
    stale_ip_permissions: NotRequired[
        "aws_sdk_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale inbound rules in the security group.</p>"""
    stale_ip_permissions_egress: NotRequired[
        "aws_sdk_ec2.types.stale_ip_permission_set.StaleIpPermissionSet"
    ]
    """<p>Information about the stale outbound rules in the security group.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC for the security group.</p>"""
