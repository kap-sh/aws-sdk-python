"""Generated from Smithy shape ``com.amazonaws.ec2#IpPermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_range_list
    import aws_sdk_ec2.types.ipv6_range_list
    import aws_sdk_ec2.types.prefix_list_id_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_id_group_pair_list


class IpPermission(TypedDict):
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers</a>).</p> <p>Use <code>-1</code> to specify all protocols. When authorizing security group rules, specifying <code>-1</code> or a protocol number other than <code>tcp</code>, <code>udp</code>, <code>icmp</code>, or <code>icmpv6</code> allows traffic on all ports, regardless of any port range you specify. For <code>tcp</code>, <code>udp</code>, and <code>icmp</code>, you must specify a port range. For <code>icmpv6</code>, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.</p>"""
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes). If the start port is -1 (all ICMP types), then the end port must be -1 (all ICMP codes).</p>"""
    user_id_group_pairs: NotRequired[
        "aws_sdk_ec2.types.user_id_group_pair_list.UserIdGroupPairList"
    ]
    """<p>The security group and Amazon Web Services account ID pairs.</p>"""
    ip_ranges: NotRequired["aws_sdk_ec2.types.ip_range_list.IpRangeList"]
    """<p>The IPv4 address ranges.</p>"""
    ipv6_ranges: NotRequired["aws_sdk_ec2.types.ipv6_range_list.Ipv6RangeList"]
    """<p>The IPv6 address ranges.</p>"""
    prefix_list_ids: NotRequired[
        "aws_sdk_ec2.types.prefix_list_id_list.PrefixListIdList"
    ]
    """<p>The prefix list IDs.</p>"""
