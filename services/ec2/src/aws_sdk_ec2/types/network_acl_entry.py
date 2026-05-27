"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.icmp_type_code
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.rule_action
    import aws_sdk_ec2.types.string


class NetworkAclEntry(TypedDict):
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 network range to allow or deny, in CIDR notation.</p>"""
    egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the rule is an egress rule (applied to traffic leaving the subnet).</p>"""
    icmp_type_code: NotRequired["aws_sdk_ec2.types.icmp_type_code.IcmpTypeCode"]
    """<p>ICMP protocol: The ICMP type and code.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 network range to allow or deny, in CIDR notation.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>TCP or UDP protocols: The range of ports the rule applies to.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol number. A value of \"-1\" means all protocols.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.rule_action.RuleAction"]
    """<p>Indicates whether to allow or deny the traffic that matches the rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number for the entry. ACL entries are processed in ascending order by rule number.</p>"""
