"""Generated from Smithy shape ``com.amazonaws.securityhub#RouteSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class RouteSetDetails(TypedDict, closed=True):
    carrier_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the carrier gateway. </p>"""
    core_network_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the core network. </p>"""
    destination_cidr_block: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The IPv4 CIDR block used for the destination match. </p>"""
    destination_ipv6_cidr_block: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The IPv6 CIDR block used for the destination match. </p>"""
    destination_prefix_list_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The prefix of the destination Amazon Web Services service. </p>"""
    egress_only_internet_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the egress-only internet gateway. </p>"""
    gateway_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of a gateway attached to your VPC. </p>"""
    instance_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of a NAT instance in your VPC. </p>"""
    instance_owner_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the Amazon Web Services account that owns the instance. </p>"""
    local_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the local gateway. </p>"""
    nat_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of a NAT gateway. </p>"""
    network_interface_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of the network interface. </p>"""
    origin: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Describes how the route was created. </p>"""
    state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The state of the route. </p>"""
    transit_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of a transit gateway. </p>"""
    vpc_peering_connection_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ID of a VPC peering connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSetDetails) -> dict:
    out: dict = {}
    if "carrier_gateway_id" in value:
        out["CarrierGatewayId"] = value["carrier_gateway_id"]
    if "core_network_arn" in value:
        out["CoreNetworkArn"] = value["core_network_arn"]
    if "destination_cidr_block" in value:
        out["DestinationCidrBlock"] = value["destination_cidr_block"]
    if "destination_ipv6_cidr_block" in value:
        out["DestinationIpv6CidrBlock"] = value["destination_ipv6_cidr_block"]
    if "destination_prefix_list_id" in value:
        out["DestinationPrefixListId"] = value["destination_prefix_list_id"]
    if "egress_only_internet_gateway_id" in value:
        out["EgressOnlyInternetGatewayId"] = value["egress_only_internet_gateway_id"]
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_owner_id" in value:
        out["InstanceOwnerId"] = value["instance_owner_id"]
    if "local_gateway_id" in value:
        out["LocalGatewayId"] = value["local_gateway_id"]
    if "nat_gateway_id" in value:
        out["NatGatewayId"] = value["nat_gateway_id"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "origin" in value:
        out["Origin"] = value["origin"]
    if "state" in value:
        out["State"] = value["state"]
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
    if "vpc_peering_connection_id" in value:
        out["VpcPeeringConnectionId"] = value["vpc_peering_connection_id"]
    return out


def deserialize_json(data: dict) -> RouteSetDetails:
    out: RouteSetDetails = {}  # type: ignore[typeddict-item]
    if "CarrierGatewayId" in data:
        out["carrier_gateway_id"] = data["CarrierGatewayId"]
    if "CoreNetworkArn" in data:
        out["core_network_arn"] = data["CoreNetworkArn"]
    if "DestinationCidrBlock" in data:
        out["destination_cidr_block"] = data["DestinationCidrBlock"]
    if "DestinationIpv6CidrBlock" in data:
        out["destination_ipv6_cidr_block"] = data["DestinationIpv6CidrBlock"]
    if "DestinationPrefixListId" in data:
        out["destination_prefix_list_id"] = data["DestinationPrefixListId"]
    if "EgressOnlyInternetGatewayId" in data:
        out["egress_only_internet_gateway_id"] = data["EgressOnlyInternetGatewayId"]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    if "InstanceOwnerId" in data:
        out["instance_owner_id"] = data["InstanceOwnerId"]
    if "LocalGatewayId" in data:
        out["local_gateway_id"] = data["LocalGatewayId"]
    if "NatGatewayId" in data:
        out["nat_gateway_id"] = data["NatGatewayId"]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "Origin" in data:
        out["origin"] = data["Origin"]
    if "State" in data:
        out["state"] = data["State"]
    if "TransitGatewayId" in data:
        out["transit_gateway_id"] = data["TransitGatewayId"]
    if "VpcPeeringConnectionId" in data:
        out["vpc_peering_connection_id"] = data["VpcPeeringConnectionId"]
    return out
