"""Generated from Smithy shape ``com.amazonaws.ec2#FirewallStatefulRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class FirewallStatefulRule(TypedDict):
    rule_group_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the stateful rule group.</p>"""
    sources: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source IP addresses, in CIDR notation.</p>"""
    destinations: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The destination IP addresses, in CIDR notation.</p>"""
    source_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The destination ports.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule action. The possible values are <code>pass</code>, <code>drop</code>, and <code>alert</code>.</p>"""
    direction: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The direction. The possible values are <code>FORWARD</code> and <code>ANY</code>.</p>"""
