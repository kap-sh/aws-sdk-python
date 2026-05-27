"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupEgressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_rule_id_list
    import aws_sdk_ec2.types.string


class RevokeSecurityGroupEgressRequest(TypedDict):
    security_group_rule_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id_list.SecurityGroupRuleIdList"
    ]
    """<p>The IDs of the security group rules.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    source_security_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify a destination security group.</p>"""
    source_security_group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify a destination security group.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify the protocol name or number.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use a set of IP permissions to specify the port.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Not supported. Use a set of IP permissions to specify the port.</p>"""
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported. Use a set of IP permissions to specify the CIDR.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The sets of IP permissions. You can't specify a destination security group and a CIDR IP address range in the same set of permissions.</p>"""
