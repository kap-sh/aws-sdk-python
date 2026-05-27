"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupIngressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_name
    import aws_sdk_ec2.types.security_group_rule_id_list
    import aws_sdk_ec2.types.string


class RevokeSecurityGroupIngressRequest(TypedDict):
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR IP address range. You can't specify this parameter when specifying a source security group.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The sets of IP permissions. You can't specify a source security group and a CIDR IP address range in the same set of permissions.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>). Use <code>-1</code> to specify all.</p>"""
    source_security_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Default VPC] The name of the source security group. You can't specify this parameter in combination with the following parameters: the CIDR IP address range, the start of the port range, the IP protocol, and the end of the port range. The source security group must be in the same VPC. To revoke a specific rule for an IP protocol and port range, use a set of IP permissions instead.</p>"""
    source_security_group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Not supported.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes).</p>"""
    security_group_rule_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id_list.SecurityGroupRuleIdList"
    ]
    """<p>The IDs of the security group rules.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
