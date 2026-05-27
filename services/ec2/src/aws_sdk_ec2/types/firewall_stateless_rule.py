"""Generated from Smithy shape ``com.amazonaws.ec2#FirewallStatelessRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.priority
    import aws_sdk_ec2.types.protocol_int_list
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class FirewallStatelessRule(TypedDict):
    rule_group_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the stateless rule group.</p>"""
    sources: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source IP addresses, in CIDR notation.</p>"""
    destinations: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The destination IP addresses, in CIDR notation.</p>"""
    source_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The destination ports.</p>"""
    protocols: NotRequired["aws_sdk_ec2.types.protocol_int_list.ProtocolIntList"]
    """<p>The protocols.</p>"""
    rule_action: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule action. The possible values are <code>pass</code>, <code>drop</code>, and <code>forward_to_site</code>.</p>"""
    priority: NotRequired["aws_sdk_ec2.types.priority.Priority"]
    """<p>The rule priority.</p>"""
