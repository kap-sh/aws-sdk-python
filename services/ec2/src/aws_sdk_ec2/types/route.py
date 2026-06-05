"""Generated from Smithy shape ``com.amazonaws.ec2#Route``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Route, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "destination_ipv6_cidr_block" in value:
        pairs.append(
            (
                f"{prefix}.DestinationIpv6CidrBlock",
                str(value["destination_ipv6_cidr_block"]),
            )
        )
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )
    if "egress_only_internet_gateway_id" in value:
        pairs.append(
            (
                f"{prefix}.EgressOnlyInternetGatewayId",
                str(value["egress_only_internet_gateway_id"]),
            )
        )
    if "gateway_id" in value:
        pairs.append((f"{prefix}.GatewayId", str(value["gateway_id"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "instance_owner_id" in value:
        pairs.append((f"{prefix}.InstanceOwnerId", str(value["instance_owner_id"])))
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "local_gateway_id" in value:
        pairs.append((f"{prefix}.LocalGatewayId", str(value["local_gateway_id"])))
    if "carrier_gateway_id" in value:
        pairs.append((f"{prefix}.CarrierGatewayId", str(value["carrier_gateway_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "origin" in value:
        import aws_sdk_ec2.types.route_origin

        aws_sdk_ec2.types.route_origin.serialize_ec2_query(
            value["origin"], pairs, f"{prefix}.Origin"
        )
    if "state" in value:
        import aws_sdk_ec2.types.route_state

        aws_sdk_ec2.types.route_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "core_network_arn" in value:
        pairs.append((f"{prefix}.CoreNetworkArn", str(value["core_network_arn"])))
    if "odb_network_arn" in value:
        pairs.append((f"{prefix}.OdbNetworkArn", str(value["odb_network_arn"])))
    if "ip_address" in value:
        pairs.append((f"{prefix}.IpAddress", str(value["ip_address"])))


def deserialize_ec2_query(el: Element) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_destination_ipv6_cidr_block = el.find("DestinationIpv6CidrBlock")
    if child_destination_ipv6_cidr_block is not None:
        out["destination_ipv6_cidr_block"] = str(
            child_destination_ipv6_cidr_block.text or ""
        )
    child_destination_prefix_list_id = el.find("DestinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    child_egress_only_internet_gateway_id = el.find("EgressOnlyInternetGatewayId")
    if child_egress_only_internet_gateway_id is not None:
        out["egress_only_internet_gateway_id"] = str(
            child_egress_only_internet_gateway_id.text or ""
        )
    child_gateway_id = el.find("GatewayId")
    if child_gateway_id is not None:
        out["gateway_id"] = str(child_gateway_id.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_owner_id = el.find("InstanceOwnerId")
    if child_instance_owner_id is not None:
        out["instance_owner_id"] = str(child_instance_owner_id.text or "")
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_carrier_gateway_id = el.find("CarrierGatewayId")
    if child_carrier_gateway_id is not None:
        out["carrier_gateway_id"] = str(child_carrier_gateway_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_origin = el.find("Origin")
    if child_origin is not None:
        import aws_sdk_ec2.types.route_origin

        out["origin"] = aws_sdk_ec2.types.route_origin.deserialize_ec2_query(
            child_origin
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.route_state

        out["state"] = aws_sdk_ec2.types.route_state.deserialize_ec2_query(child_state)
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_core_network_arn = el.find("CoreNetworkArn")
    if child_core_network_arn is not None:
        out["core_network_arn"] = str(child_core_network_arn.text or "")
    child_odb_network_arn = el.find("OdbNetworkArn")
    if child_odb_network_arn is not None:
        out["odb_network_arn"] = str(child_odb_network_arn.text or "")
    child_ip_address = el.find("IpAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    return out
