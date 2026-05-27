"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkAclEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.icmp_type_code
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.network_acl_id
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.rule_action
    import aws_sdk_ec2.types.string


class CreateNetworkAclEntryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_acl_id: NotRequired["aws_sdk_ec2.types.network_acl_id.NetworkAclId"]
    """<p>The ID of the network ACL.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number for the entry (for example, 100). ACL entries are processed in ascending order by rule number.</p> <p>Constraints: Positive integer from 1 to 32766. The range 32767 to 65535 is reserved for internal use.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol number. A value of \"-1\" means all protocols. If you specify \"-1\" or a protocol number other than \"6\" (TCP), \"17\" (UDP), or \"1\" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol \"58\" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.rule_action.RuleAction"]
    """<p>Indicates whether to allow or deny the traffic that matches the rule.</p>"""
    egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is an egress rule (rule is applied to traffic leaving the subnet).</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 network range to allow or deny, in CIDR notation (for example <code>172.16.0.0/24</code>). We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 network range to allow or deny, in CIDR notation (for example <code>2001:db8:1234:1a00::/64</code>).</p>"""
    icmp_type_code: NotRequired["aws_sdk_ec2.types.icmp_type_code.IcmpTypeCode"]
    """<p>ICMP protocol: The ICMP or ICMPv6 type and code. Required if specifying protocol 1 (ICMP) or protocol 58 (ICMPv6) with an IPv6 CIDR block.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>TCP or UDP protocols: The range of ports the rule applies to. Required if specifying protocol 6 (TCP) or 17 (UDP).</p>"""
