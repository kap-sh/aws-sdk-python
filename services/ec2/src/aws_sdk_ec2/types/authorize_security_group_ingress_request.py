"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupIngressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_permission_list
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_name
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class AuthorizeSecurityGroupIngressRequest(TypedDict):
    cidr_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR format.</p> <note> <p> Amazon Web Services <a href=\"https://en.wikipedia.org/wiki/Canonicalization\">canonicalizes</a> IPv4 and IPv6 CIDRs. For example, if you specify 100.68.0.18/18 for the CIDR block, Amazon Web Services canonicalizes the CIDR block to 100.68.0.0/18. Any subsequent DescribeSecurityGroups and DescribeSecurityGroupRules calls will return the canonicalized form of the CIDR block. Additionally, if you attempt to add another rule with the non-canonical form of the CIDR (such as 100.68.0.18/18) and there is already a rule for the canonicalized form of the CIDR block (such as 100.68.0.0/18), the API throws an duplicate rule error.</p> </note> <p>To specify an IPv6 address range, use IP permissions instead.</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP, this is the ICMP type or -1 (all ICMP types).</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. For security groups for a default VPC you can specify either the ID or the name of the security group. For security groups for a nondefault VPC, you must specify the ID of the security group.</p>"""
    ip_permissions: NotRequired["aws_sdk_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The permissions for the security group rules.</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>). To specify all protocols, use <code>-1</code>.</p> <p>To specify <code>icmpv6</code>, use IP permissions instead.</p> <p>If you specify a protocol other than one of the supported values, traffic is allowed on all ports, regardless of any ports that you specify.</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>"""
    source_security_group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Default VPC] The name of the source security group.</p> <p>The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, specify a set of IP permissions instead.</p>"""
    source_security_group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID for the source security group, if the source security group is in a different account.</p> <p>The rule grants full ICMP, UDP, and TCP access. To create a rule with a specific protocol and port range, use IP permissions instead.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p> <p>To specify multiple rules and descriptions for the rules, use IP permissions instead.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags applied to the security group rule.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
