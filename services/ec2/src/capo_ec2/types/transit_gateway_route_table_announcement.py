"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_attachment_id
    import capo_ec2.types.transit_gateway_id
    import capo_ec2.types.transit_gateway_route_table_announcement_direction
    import capo_ec2.types.transit_gateway_route_table_announcement_id
    import capo_ec2.types.transit_gateway_route_table_announcement_state
    import capo_ec2.types.transit_gateway_route_table_id


class TransitGatewayRouteTableAnnouncement(TypedDict, closed=True):
    transit_gateway_route_table_announcement_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_announcement_id.TransitGatewayRouteTableAnnouncementId"
    ]
    """<p>The ID of the transit gateway route table announcement.</p>"""
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    core_network_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the core network for the transit gateway route table announcement.</p>"""
    peer_transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the peer transit gateway.</p>"""
    peer_core_network_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the core network ID for the peer.</p>"""
    peering_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the peering attachment.</p>"""
    announcement_direction: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_announcement_direction.TransitGatewayRouteTableAnnouncementDirection"
    ]
    """<p>The direction for the route table announcement.</p>"""
    transit_gateway_route_table_id: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_announcement_state.TransitGatewayRouteTableAnnouncementState"
    ]
    """<p>The state of the transit gateway announcement.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The timestamp when the transit gateway route table announcement was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The key-value pairs associated with the route table announcement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTableAnnouncement,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_table_announcement_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableAnnouncementId",
                str(value["transit_gateway_route_table_announcement_id"]),
            )
        )
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "core_network_id" in value:
        pairs.append((f"{key_prefix}CoreNetworkId", str(value["core_network_id"])))
    if "peer_transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}PeerTransitGatewayId", str(value["peer_transit_gateway_id"]))
        )
    if "peer_core_network_id" in value:
        pairs.append(
            (f"{key_prefix}PeerCoreNetworkId", str(value["peer_core_network_id"]))
        )
    if "peering_attachment_id" in value:
        pairs.append(
            (f"{key_prefix}PeeringAttachmentId", str(value["peering_attachment_id"]))
        )
    if "announcement_direction" in value:
        import capo_ec2.types.transit_gateway_route_table_announcement_direction

        capo_ec2.types.transit_gateway_route_table_announcement_direction.serialize_ec2_query(
            value["announcement_direction"], pairs, f"{key_prefix}AnnouncementDirection"
        )
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_route_table_announcement_state

        capo_ec2.types.transit_gateway_route_table_announcement_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "creation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableAnnouncement:
    out: TransitGatewayRouteTableAnnouncement = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_announcement_id = el.find(
        "TransitGatewayRouteTableAnnouncementId"
    )
    if child_transit_gateway_route_table_announcement_id is not None:
        out["transit_gateway_route_table_announcement_id"] = str(
            child_transit_gateway_route_table_announcement_id.text or ""
        )
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_core_network_id = el.find("CoreNetworkId")
    if child_core_network_id is not None:
        out["core_network_id"] = str(child_core_network_id.text or "")
    child_peer_transit_gateway_id = el.find("PeerTransitGatewayId")
    if child_peer_transit_gateway_id is not None:
        out["peer_transit_gateway_id"] = str(child_peer_transit_gateway_id.text or "")
    child_peer_core_network_id = el.find("PeerCoreNetworkId")
    if child_peer_core_network_id is not None:
        out["peer_core_network_id"] = str(child_peer_core_network_id.text or "")
    child_peering_attachment_id = el.find("PeeringAttachmentId")
    if child_peering_attachment_id is not None:
        out["peering_attachment_id"] = str(child_peering_attachment_id.text or "")
    child_announcement_direction = el.find("AnnouncementDirection")
    if child_announcement_direction is not None:
        import capo_ec2.types.transit_gateway_route_table_announcement_direction

        out["announcement_direction"] = (
            capo_ec2.types.transit_gateway_route_table_announcement_direction.deserialize_ec2_query(
                child_announcement_direction
            )
        )
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_route_table_announcement_state

        out["state"] = (
            capo_ec2.types.transit_gateway_route_table_announcement_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
