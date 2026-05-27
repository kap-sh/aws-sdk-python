"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.string


class SecurityGroupRuleRequest(TypedDict):
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>). </p> <p>Use <code>-1</code> to specify all protocols.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p>"""
    cidr_ipv4: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR range. To specify a single IPv4 address, use the /32 prefix length. </p>"""
    cidr_ipv6: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    referenced_group_id: NotRequired[
        "aws_sdk_ec2.types.security_group_id.SecurityGroupId"
    ]
    """<p>The ID of the security group that is referenced in the security group rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the security group rule.</p>"""
