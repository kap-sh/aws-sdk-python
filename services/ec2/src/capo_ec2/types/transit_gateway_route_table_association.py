"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_association_state
    import capo_ec2.types.transit_gateway_attachment_resource_type


class TransitGatewayRouteTableAssociation(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the attachment.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_resource_type.TransitGatewayAttachmentResourceType"
    ]
    """<p>The resource type. Note that the <code>tgw-peering</code> resource type has been deprecated.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_association_state.TransitGatewayAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTableAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_type" in value:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        capo_ec2.types.transit_gateway_attachment_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_association_state

        capo_ec2.types.transit_gateway_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableAssociation:
    out: TransitGatewayRouteTableAssociation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("transitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.transit_gateway_attachment_resource_type

        out["resource_type"] = (
            capo_ec2.types.transit_gateway_attachment_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_association_state

        out["state"] = (
            capo_ec2.types.transit_gateway_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
