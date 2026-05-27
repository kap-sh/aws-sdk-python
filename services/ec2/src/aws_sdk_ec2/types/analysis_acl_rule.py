"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisAclRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.port_range
    import aws_sdk_ec2.types.string


class AnalysisAclRule(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address range, in CIDR notation.</p>"""
    egress: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the rule is an outbound rule.</p>"""
    port_range: NotRequired["aws_sdk_ec2.types.port_range.PortRange"]
    """<p>The range of ports.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Indicates whether to allow or deny traffic that matches the rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The rule number.</p>"""
