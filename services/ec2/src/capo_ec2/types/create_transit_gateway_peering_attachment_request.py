"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayPeeringAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.create_transit_gateway_peering_attachment_request_options
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.transit_association_gateway_id
    import capo_ec2.types.transit_gateway_id


class CreateTransitGatewayPeeringAttachmentRequest(TypedDict, closed=True):
    transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    peer_transit_gateway_id: NotRequired[
        "capo_ec2.types.transit_association_gateway_id.TransitAssociationGatewayId"
    ]
    """<p>The ID of the peer transit gateway with which to create the peering attachment.</p>"""
    peer_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the peer transit gateway.</p>"""
    peer_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region where the peer transit gateway is located.</p>"""
    options: NotRequired[
        "capo_ec2.types.create_transit_gateway_peering_attachment_request_options.CreateTransitGatewayPeeringAttachmentRequestOptions"
    ]
    """<p>Requests a transit gateway peering attachment.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the transit gateway peering attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayPeeringAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}TransitGatewayId", str(value["transit_gateway_id"]))
        )
    if "peer_transit_gateway_id" in value:
        pairs.append(
            (f"{key_prefix}PeerTransitGatewayId", str(value["peer_transit_gateway_id"]))
        )
    if "peer_account_id" in value:
        pairs.append((f"{key_prefix}PeerAccountId", str(value["peer_account_id"])))
    if "peer_region" in value:
        pairs.append((f"{key_prefix}PeerRegion", str(value["peer_region"])))
    if "options" in value:
        import capo_ec2.types.create_transit_gateway_peering_attachment_request_options

        capo_ec2.types.create_transit_gateway_peering_attachment_request_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayPeeringAttachmentRequest:
    out: CreateTransitGatewayPeeringAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_id = el.find("TransitGatewayId")
    if child_transit_gateway_id is not None:
        out["transit_gateway_id"] = str(child_transit_gateway_id.text or "")
    child_peer_transit_gateway_id = el.find("PeerTransitGatewayId")
    if child_peer_transit_gateway_id is not None:
        out["peer_transit_gateway_id"] = str(child_peer_transit_gateway_id.text or "")
    child_peer_account_id = el.find("PeerAccountId")
    if child_peer_account_id is not None:
        out["peer_account_id"] = str(child_peer_account_id.text or "")
    child_peer_region = el.find("PeerRegion")
    if child_peer_region is not None:
        out["peer_region"] = str(child_peer_region.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.create_transit_gateway_peering_attachment_request_options

        out["options"] = (
            capo_ec2.types.create_transit_gateway_peering_attachment_request_options.deserialize_ec2_query(
                child_options
            )
        )
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
