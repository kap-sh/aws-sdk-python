"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_pool_id
    import aws_sdk_ec2.types.local_gateway_route_state
    import aws_sdk_ec2.types.local_gateway_route_type
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class LocalGatewayRoute(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    type: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_type.LocalGatewayRouteType"
    ]
    """<p>The route type.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_state.LocalGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    coip_pool_id: NotRequired["aws_sdk_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The ID of the customer-owned address pool.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    destination_prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p> The ID of the prefix list. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "type" in value:
        import aws_sdk_ec2.types.local_gateway_route_type

        aws_sdk_ec2.types.local_gateway_route_type.serialize_ec2_query(
            value["type"], pairs, f"{prefix}.Type"
        )
    if "state" in value:
        import aws_sdk_ec2.types.local_gateway_route_state

        aws_sdk_ec2.types.local_gateway_route_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "local_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableId",
                str(value["local_gateway_route_table_id"]),
            )
        )
    if "local_gateway_route_table_arn" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayRouteTableArn",
                str(value["local_gateway_route_table_arn"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "coip_pool_id" in value:
        pairs.append((f"{prefix}.CoipPoolId", str(value["coip_pool_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "destination_prefix_list_id" in value:
        pairs.append(
            (
                f"{prefix}.DestinationPrefixListId",
                str(value["destination_prefix_list_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRoute:
    out: LocalGatewayRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_local_gateway_virtual_interface_group_id = el.find(
        "LocalGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    child_type = el.find("Type")
    if child_type is not None:
        import aws_sdk_ec2.types.local_gateway_route_type

        out["type"] = aws_sdk_ec2.types.local_gateway_route_type.deserialize_ec2_query(
            child_type
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.local_gateway_route_state

        out["state"] = (
            aws_sdk_ec2.types.local_gateway_route_state.deserialize_ec2_query(
                child_state
            )
        )
    child_local_gateway_route_table_id = el.find("LocalGatewayRouteTableId")
    if child_local_gateway_route_table_id is not None:
        out["local_gateway_route_table_id"] = str(
            child_local_gateway_route_table_id.text or ""
        )
    child_local_gateway_route_table_arn = el.find("LocalGatewayRouteTableArn")
    if child_local_gateway_route_table_arn is not None:
        out["local_gateway_route_table_arn"] = str(
            child_local_gateway_route_table_arn.text or ""
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_coip_pool_id = el.find("CoipPoolId")
    if child_coip_pool_id is not None:
        out["coip_pool_id"] = str(child_coip_pool_id.text or "")
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_destination_prefix_list_id = el.find("DestinationPrefixListId")
    if child_destination_prefix_list_id is not None:
        out["destination_prefix_list_id"] = str(
            child_destination_prefix_list_id.text or ""
        )
    return out
