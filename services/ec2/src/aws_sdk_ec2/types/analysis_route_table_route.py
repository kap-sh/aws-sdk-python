"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisRouteTableRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string


class AnalysisRouteTableRoute(TypedDict):
    destination_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination IPv4 address, in CIDR notation.</p>"""
    destination_prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix of the Amazon Web Services service.</p>"""
    egress_only_internet_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an egress-only internet gateway.</p>"""
    gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the gateway, such as an internet gateway or virtual private gateway.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance, such as a NAT instance.</p>"""
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a NAT gateway.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a network interface.</p>"""
    origin: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Describes how the route was created. The following are the possible values:</p> <ul> <li> <p>CreateRouteTable - The route was automatically created when the route table was created.</p> </li> <li> <p>CreateRoute - The route was manually added to the route table.</p> </li> <li> <p>EnableVgwRoutePropagation - The route was propagated by route propagation.</p> </li> </ul>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a transit gateway.</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a VPC peering connection.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state. The following are the possible values:</p> <ul> <li> <p>active</p> </li> <li> <p>blackhole</p> </li> </ul>"""
    carrier_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a carrier gateway.</p>"""
    core_network_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of a core network.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a local gateway.</p>"""
