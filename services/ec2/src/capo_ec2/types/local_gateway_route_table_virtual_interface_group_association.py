"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVirtualInterfaceGroupAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_id
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id
    import capo_ec2.types.local_gateway_virtual_interface_group_id
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class LocalGatewayRouteTableVirtualInterfaceGroupAssociation(TypedDict, closed=True):
    local_gateway_route_table_virtual_interface_group_association_id: NotRequired[
        "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    local_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    local_gateway_route_table_id: NotRequired[
        "capo_ec2.types.local_gateway_id.LocalGatewayId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table for the virtual interface group.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface group association.</p>"""
    state: NotRequired["capo_ec2.types.string.String"]
    """<p>The state of the association.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTableVirtualInterfaceGroupAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_virtual_interface_group_association_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayRouteTableVirtualInterfaceGroupAssociationId",
                str(
                    value[
                        "local_gateway_route_table_virtual_interface_group_association_id"
                    ]
                ),
            )
        )
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "local_gateway_id" in value:
        pairs.append((f"{key_prefix}LocalGatewayId", str(value["local_gateway_id"])))
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
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> LocalGatewayRouteTableVirtualInterfaceGroupAssociation:
    out: LocalGatewayRouteTableVirtualInterfaceGroupAssociation = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_virtual_interface_group_association_id = el.find(
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    )
    if (
        child_local_gateway_route_table_virtual_interface_group_association_id
        is not None
    ):
        out["local_gateway_route_table_virtual_interface_group_association_id"] = str(
            child_local_gateway_route_table_virtual_interface_group_association_id.text
            or ""
        )
    child_local_gateway_virtual_interface_group_id = el.find(
        "LocalGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    child_local_gateway_id = el.find("LocalGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
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
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
