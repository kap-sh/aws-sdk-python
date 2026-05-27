"""Generated from Smithy shape ``com.amazonaws.ec2#Route``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway_id
    import aws_sdk_ec2.types.core_network_arn
    import aws_sdk_ec2.types.odb_network_arn
    import aws_sdk_ec2.types.route_origin
    import aws_sdk_ec2.types.route_state
    import aws_sdk_ec2.types.string


class Route(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block used for the destination match.</p>"""
    destination_ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block used for the destination match.</p>"""
    destination_prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix of the Amazon Web Services service.</p>"""
    egress_only_internet_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the egress-only internet gateway.</p>"""
    gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a gateway attached to your VPC.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a NAT instance in your VPC.</p>"""
    instance_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of Amazon Web Services account that owns the instance.</p>"""
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a NAT gateway.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a transit gateway.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    carrier_gateway_id: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_id.CarrierGatewayId"
    ]
    """<p>The ID of the carrier gateway.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    origin: NotRequired["aws_sdk_ec2.types.route_origin.RouteOrigin"]
    """<p>Describes how the route was created.</p> <ul> <li> <p> <code>CreateRouteTable</code> - The route was automatically created when the route table was created.</p> </li> <li> <p> <code>CreateRoute</code> - The route was manually added to the route table.</p> </li> <li> <p> <code>EnableVgwRoutePropagation</code> - The route was propagated by route propagation.</p> </li> <li> <p> <code>Advertisement</code> - The route was created dynamically by Amazon VPC Route Server.</p> </li> </ul>"""
    state: NotRequired["aws_sdk_ec2.types.route_state.RouteState"]
    """<p>The state of the route. The <code>blackhole</code> state indicates that the route's target isn't available (for example, the specified gateway isn't attached to the VPC, or the specified NAT instance has been terminated).</p>"""
    vpc_peering_connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a VPC peering connection.</p>"""
    core_network_arn: NotRequired["aws_sdk_ec2.types.core_network_arn.CoreNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the core network.</p>"""
    odb_network_arn: NotRequired["aws_sdk_ec2.types.odb_network_arn.OdbNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network.</p>"""
    ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The next hop IP address for routes propagated by VPC Route Server into VPC route tables.</p>"""
