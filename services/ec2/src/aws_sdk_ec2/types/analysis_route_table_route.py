"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisRouteTableRoute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisRouteTableRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_cidr" in value:
        pairs.append((f"{prefix}.DestinationCidr", str(value["destination_cidr"])))
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
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "origin" in value:
        pairs.append((f"{prefix}.Origin", str(value["origin"])))
    if "transit_gateway_id" in value:
        pairs.append((f"{prefix}.TransitGatewayId", str(value["transit_gateway_id"])))
    if "vpc_peering_connection_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcPeeringConnectionId",
                str(value["vpc_peering_connection_id"]),
            )
        )
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "carrier_gateway_id" in value:
        pairs.append((f"{prefix}.CarrierGatewayId", str(value["carrier_gateway_id"])))
    if "core_network_arn" in value:
        pairs.append((f"{prefix}.CoreNetworkArn", str(value["core_network_arn"])))
    if "local_gateway_id" in value:
        pairs.append((f"{prefix}.LocalGatewayId", str(value["local_gateway_id"])))


def deserialize_ec2_query(el: Element) -> AnalysisRouteTableRoute:
    out: AnalysisRouteTableRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr = el.find("DestinationCidr")
    if child_destination_cidr is not None:
        out["destination_cidr"] = str(child_destination_cidr.text or "")
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
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_origin = el.find("Origin")
    if child_origin is not None:
        out["origin"] = str(child_origin.text or "")
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_vpc_peering_connection_id = el.find("VpcPeeringConnectionId")
    if child_vpc_peering_connection_id is not None:
        out["vpc_peering_connection_id"] = str(
            child_vpc_peering_connection_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_carrier_gateway_id = el.find("CarrierGatewayId")
    if child_carrier_gateway_id is not None:
        out["carrier_gateway_id"] = str(child_carrier_gateway_id.text or "")
    child_core_network_arn = el.find("CoreNetworkArn")
    if child_core_network_arn is not None:
        out["core_network_arn"] = str(child_core_network_arn.text or "")
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    return out
