"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_pool_id
    import capo_ec2.types.local_gateway_route_state
    import capo_ec2.types.local_gateway_route_type
    import capo_ec2.types.local_gateway_routetable_id
    import capo_ec2.types.local_gateway_virtual_interface_group_id
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class LocalGatewayRoute(TypedDict, closed=True):
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    type: NotRequired["capo_ec2.types.local_gateway_route_type.LocalGatewayRouteType"]
    """<p>The route type.</p>"""
    state: NotRequired[
        "capo_ec2.types.local_gateway_route_state.LocalGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""
    local_gateway_route_table_id: NotRequired[
        "capo_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    coip_pool_id: NotRequired["capo_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The ID of the customer-owned address pool.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    destination_prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p> The ID of the prefix list. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "type" in value:
        import capo_ec2.types.local_gateway_route_type

        capo_ec2.types.local_gateway_route_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "state" in value:
        import capo_ec2.types.local_gateway_route_state

        capo_ec2.types.local_gateway_route_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "local_gateway_route_table_arn" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableArn",
                str(value["local_gateway_route_table_arn"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "coip_pool_id" in value:
        pairs.append((f"{key_prefix}CoipPoolId", str(value["coip_pool_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRoute:
    out: LocalGatewayRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("destinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_local_gateway_virtual_interface_group_id = el.find(
        "localGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.local_gateway_route_type

        out["type"] = capo_ec2.types.local_gateway_route_type.deserialize_ec2_query(
            child_type
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.local_gateway_route_state

        out["state"] = capo_ec2.types.local_gateway_route_state.deserialize_ec2_query(
            child_state
        )
    child_local_gateway_route_table_id = el.find("localGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_local_gateway_route_table_arn = el.find("localGatewayRouteTableArn")
    if child_local_gateway_route_table_arn is not None:
        out["local_gateway_route_table_arn"] = str(
            child_local_gateway_route_table_arn.text or ""
        )
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_coip_pool_id = el.find("coipPoolId")
    if child_coip_pool_id is not None:
        out["coip_pool_id"] = str(child_coip_pool_id.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_destination_prefix_list_id = el.find("destinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    return out
