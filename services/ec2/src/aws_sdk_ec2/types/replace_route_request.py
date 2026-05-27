"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.carrier_gateway_id
    import aws_sdk_ec2.types.core_network_arn
    import aws_sdk_ec2.types.egress_only_internet_gateway_id
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.nat_gateway_id
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.odb_network_arn
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.route_gateway_id
    import aws_sdk_ec2.types.route_table_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.vpc_endpoint_id
    import aws_sdk_ec2.types.vpc_peering_connection_id


class ReplaceRouteRequest(TypedDict):
    destination_prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list for the route.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_ec2.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.</p>"""
    local_target: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to reset the local route to its default target (<code>local</code>).</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of a transit gateway.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    carrier_gateway_id: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_id.CarrierGatewayId"
    ]
    """<p>[IPv4 traffic only] The ID of a carrier gateway.</p>"""
    core_network_arn: NotRequired["aws_sdk_ec2.types.core_network_arn.CoreNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the core network.</p>"""
    odb_network_arn: NotRequired["aws_sdk_ec2.types.odb_network_arn.OdbNetworkArn"]
    """<p>The Amazon Resource Name (ARN) of the ODB network.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.</p>"""
    gateway_id: NotRequired["aws_sdk_ec2.types.route_gateway_id.RouteGatewayId"]
    """<p>The ID of an internet gateway or virtual private gateway.</p>"""
    destination_ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR address block used for the destination match. The value that you provide must match the CIDR of an existing route in the table.</p>"""
    egress_only_internet_gateway_id: NotRequired[
        "aws_sdk_ec2.types.egress_only_internet_gateway_id.EgressOnlyInternetGatewayId"
    ]
    """<p>[IPv6 traffic only] The ID of an egress-only internet gateway.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of a NAT instance in your VPC.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of a network interface.</p>"""
    vpc_peering_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_id.VpcPeeringConnectionId"
    ]
    """<p>The ID of a VPC peering connection.</p>"""
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>[IPv4 traffic only] The ID of a NAT gateway.</p>"""
