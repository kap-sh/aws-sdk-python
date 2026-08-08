"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_route_attachment_list
    import capo_ec2.types.transit_gateway_route_state
    import capo_ec2.types.transit_gateway_route_table_announcement_id
    import capo_ec2.types.transit_gateway_route_type


class TransitGatewayRoute(TypedDict, closed=True):
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list used for destination matches.</p>"""
    transit_gateway_route_table_announcement_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement. </p>"""
    transit_gateway_attachments: NotRequired[
        "capo_ec2.types.transit_gateway_route_attachment_list.TransitGatewayRouteAttachmentList"
    ]
    """<p>The attachments.</p>"""
    type: NotRequired[
        "capo_ec2.types.transit_gateway_route_type.TransitGatewayRouteType"
    ]
    """<p>The route type.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_route_state.TransitGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "transit_gateway_route_table_announcement_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableAnnouncementId",
                str(value["transit_gateway_route_table_announcement_id"]),
            )
        )
    if "transit_gateway_attachments" in value:
        import capo_ec2.types.transit_gateway_route_attachment_list

        capo_ec2.types.transit_gateway_route_attachment_list.serialize_ec2_query(
            value["transit_gateway_attachments"],
            pairs,
            f"{key_prefix}TransitGatewayAttachments",
        )
    if "type" in value:
        import capo_ec2.types.transit_gateway_route_type

        capo_ec2.types.transit_gateway_route_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_route_state

        capo_ec2.types.transit_gateway_route_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRoute:
    out: TransitGatewayRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("destinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_transit_gateway_route_table_announcement_id = el.find(
        "transitGatewayRouteTableAnnouncementId"
    )
    if child_transit_gateway_route_table_announcement_id is not None:
        out["transit_gateway_route_table_announcement_id"] = str(
            child_transit_gateway_route_table_announcement_id.text or ""
        )
    if el.find("transitGatewayAttachments") is not None:
        import capo_ec2.types.transit_gateway_route_attachment_list

        out["transit_gateway_attachments"] = (
            capo_ec2.types.transit_gateway_route_attachment_list.deserialize_ec2_query(
                el, "transitGatewayAttachments"
            )
        )
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.transit_gateway_route_type

        out["type"] = capo_ec2.types.transit_gateway_route_type.deserialize_ec2_query(
            child_type
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_route_state

        out["state"] = capo_ec2.types.transit_gateway_route_state.deserialize_ec2_query(
            child_state
        )
    return out
