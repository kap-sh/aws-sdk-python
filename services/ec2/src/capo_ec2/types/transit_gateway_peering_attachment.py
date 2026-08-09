"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.peering_attachment_status
    import capo_ec2.types.peering_tgw_info
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transit_gateway_attachment_state
    import capo_ec2.types.transit_gateway_peering_attachment_options


class TransitGatewayPeeringAttachment(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway peering attachment.</p>"""
    accepter_transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the accepter transit gateway attachment.</p>"""
    requester_tgw_info: NotRequired["capo_ec2.types.peering_tgw_info.PeeringTgwInfo"]
    """<p>Information about the requester transit gateway.</p>"""
    accepter_tgw_info: NotRequired["capo_ec2.types.peering_tgw_info.PeeringTgwInfo"]
    """<p>Information about the accepter transit gateway.</p>"""
    options: NotRequired[
        "capo_ec2.types.transit_gateway_peering_attachment_options.TransitGatewayPeeringAttachmentOptions"
    ]
    """<p>Details about the transit gateway peering attachment.</p>"""
    status: NotRequired[
        "capo_ec2.types.peering_attachment_status.PeeringAttachmentStatus"
    ]
    """<p>The status of the transit gateway peering attachment.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_state.TransitGatewayAttachmentState"
    ]
    """<p>The state of the transit gateway peering attachment. Note that the <code>initiating</code> state has been deprecated.</p>"""
    creation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time the transit gateway peering attachment was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway peering attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPeeringAttachment, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "accepter_transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}AccepterTransitGatewayAttachmentId",
                str(value["accepter_transit_gateway_attachment_id"]),
            )
        )
    if "requester_tgw_info" in value:
        import capo_ec2.types.peering_tgw_info

        capo_ec2.types.peering_tgw_info.serialize_ec2_query(
            value["requester_tgw_info"], pairs, f"{key_prefix}RequesterTgwInfo"
        )
    if "accepter_tgw_info" in value:
        import capo_ec2.types.peering_tgw_info

        capo_ec2.types.peering_tgw_info.serialize_ec2_query(
            value["accepter_tgw_info"], pairs, f"{key_prefix}AccepterTgwInfo"
        )
    if "options" in value:
        import capo_ec2.types.transit_gateway_peering_attachment_options

        capo_ec2.types.transit_gateway_peering_attachment_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "status" in value:
        import capo_ec2.types.peering_attachment_status

        capo_ec2.types.peering_attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_attachment_state

        capo_ec2.types.transit_gateway_attachment_state.serialize_ec2_query(
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


def deserialize_ec2_query(el: Element) -> TransitGatewayPeeringAttachment:
    out: TransitGatewayPeeringAttachment = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_accepter_transit_gateway_attachment_id = el.find(
        "accepterTransitGatewayAttachmentId"
    )
    if child_accepter_transit_gateway_attachment_id is not None:
        out["accepter_transit_gateway_attachment_id"] = str(
            child_accepter_transit_gateway_attachment_id.text or ""
        )
    child_requester_tgw_info = el.find("requesterTgwInfo")
    if child_requester_tgw_info is not None:
        import capo_ec2.types.peering_tgw_info

        out["requester_tgw_info"] = (
            capo_ec2.types.peering_tgw_info.deserialize_ec2_query(
                child_requester_tgw_info
            )
        )
    child_accepter_tgw_info = el.find("accepterTgwInfo")
    if child_accepter_tgw_info is not None:
        import capo_ec2.types.peering_tgw_info

        out["accepter_tgw_info"] = (
            capo_ec2.types.peering_tgw_info.deserialize_ec2_query(
                child_accepter_tgw_info
            )
        )
    child_options = el.find("options")
    if child_options is not None:
        import capo_ec2.types.transit_gateway_peering_attachment_options

        out["options"] = (
            capo_ec2.types.transit_gateway_peering_attachment_options.deserialize_ec2_query(
                child_options
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.peering_attachment_status

        out["status"] = capo_ec2.types.peering_attachment_status.deserialize_ec2_query(
            child_status
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_attachment_state

        out["state"] = (
            capo_ec2.types.transit_gateway_attachment_state.deserialize_ec2_query(
                child_state
            )
        )
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.date_time

        out["creation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_creation_time
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
