"""Generated from Smithy shape ``com.amazonaws.ec2#StaleIpPermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ip_ranges
    import aws_sdk_ec2.types.prefix_list_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.user_id_group_pair_set


class StaleIpPermission(TypedDict):
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the start of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP type or -1 (all ICMP types).</p>"""
    ip_protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP protocol name (<code>tcp</code>, <code>udp</code>, <code>icmp</code>, <code>icmpv6</code>) or number (see <a href=\"http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml\">Protocol Numbers)</a>.</p>"""
    ip_ranges: NotRequired["aws_sdk_ec2.types.ip_ranges.IpRanges"]
    """<p>The IP ranges. Not applicable for stale security group rules.</p>"""
    prefix_list_ids: NotRequired["aws_sdk_ec2.types.prefix_list_id_set.PrefixListIdSet"]
    """<p>The prefix list IDs. Not applicable for stale security group rules.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>If the protocol is TCP or UDP, this is the end of the port range. If the protocol is ICMP or ICMPv6, this is the ICMP code or -1 (all ICMP codes).</p>"""
    user_id_group_pairs: NotRequired[
        "aws_sdk_ec2.types.user_id_group_pair_set.UserIdGroupPairSet"
    ]
    """<p>The security group pairs. Returns the ID of the referenced security group and VPC, and the ID and status of the VPC peering connection.</p>"""
