"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupEgressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class AuthorizeSecurityGroupEgressRequest(TypedDict):
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags applied to the security group rule.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    source_security_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    source_security_group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use IP permissions instead.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The permissions for the security group rules.</p>"""
