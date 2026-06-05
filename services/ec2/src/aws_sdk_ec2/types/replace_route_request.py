"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceRouteRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )
    if "vpc_endpoint_id" in value:
        pairs.append((f"{prefix}.VpcEndpointId", str(value["vpc_endpoint_id"])))
    if "local_target" in value:
        pairs.append(
            (f"{prefix}.LocalTarget", "true" if value["local_target"] else "false")
        )
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "local_gateway_id" in value:
        pairs.append((f"{prefix}.LocalGatewayId", str(value["local_gateway_id"])))
    if "carrier_gateway_id" in value:
        pairs.append((f"{prefix}.CarrierGatewayId", str(value["carrier_gateway_id"])))
    if "core_network_arn" in value:
        pairs.append((f"{prefix}.CoreNetworkArn", str(value["core_network_arn"])))
    if "odb_network_arn" in value:
        pairs.append((f"{prefix}.OdbNetworkArn", str(value["odb_network_arn"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "route_table_id" in value:
        pairs.append((f"{prefix}.RouteTableId", str(value["route_table_id"])))
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "gateway_id" in value:
        pairs.append((f"{prefix}.GatewayId", str(value["gateway_id"])))
    if "destination_ipv6_cidr_block" in value:
        pairs.append(
            (
                f"{prefix}.DestinationIpv6CidrBlock",
                str(value["destination_ipv6_cidr_block"]),
            )
        )
    if "egress_only_internet_gateway_id" in value:
        pairs.append(
            (
                f"{prefix}.EgressOnlyInternetGatewayId",
                str(value["egress_only_internet_gateway_id"]),
            )
        )
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))


def deserialize_ec2_query(el: Element) -> ReplaceRouteRequest:
    out: ReplaceRouteRequest = {}  # type: ignore[typeddict-item]
    child_destination_prefix_list_id = el.find("DestinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    child_vpc_endpoint_id = el.find("VpcEndpointId")
    if child_vpc_endpoint_id is not None:
        out["vpc_endpoint_id"] = str(child_vpc_endpoint_id.text or "")
    child_local_target = el.find("LocalTarget")
    if child_local_target is not None:
        out["local_target"] = (child_local_target.text or "").lower() == "true"
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_carrier_gateway_id = el.find("CarrierGatewayId")
    if child_carrier_gateway_id is not None:
        out["carrier_gateway_id"] = str(child_carrier_gateway_id.text or "")
    child_core_network_arn = el.find("CoreNetworkArn")
    if child_core_network_arn is not None:
        out["core_network_arn"] = str(child_core_network_arn.text or "")
    child_odb_network_arn = el.find("OdbNetworkArn")
    if child_odb_network_arn is not None:
        out["odb_network_arn"] = str(child_odb_network_arn.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_gateway_id = el.find("GatewayId")
    if child_gateway_id is not None:
        out["gateway_id"] = str(child_gateway_id.text or "")
    child_destination_ipv6_cidr_block = el.find("DestinationIpv6CidrBlock")
    if child_destination_ipv6_cidr_block is not None:
        out["destination_ipv6_cidr_block"] = str(
            child_destination_ipv6_cidr_block.text or ""
        )
    child_egress_only_internet_gateway_id = el.find("EgressOnlyInternetGatewayId")
    if child_egress_only_internet_gateway_id is not None:
        out["egress_only_internet_gateway_id"] = str(
            child_egress_only_internet_gateway_id.text or ""
        )
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    return out
