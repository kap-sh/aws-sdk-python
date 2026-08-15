"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_association_state


class TransitGatewayAttachmentAssociation(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the route table for the transit gateway.</p>"""
    transit_gateway_policy_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway policy table associated with the attachment.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_association_state.TransitGatewayAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "transit_gateway_policy_table_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayPolicyTableId",
                str(value["transit_gateway_policy_table_id"]),
            )
        )
    if "state" in value:
        import capo_ec2.types.transit_gateway_association_state

        capo_ec2.types.transit_gateway_association_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentAssociation:
    out: TransitGatewayAttachmentAssociation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("transitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_transit_gateway_policy_table_id = el.find("transitGatewayPolicyTableId")
    if child_transit_gateway_policy_table_id is not None:
        out["transit_gateway_policy_table_id"] = str(
            child_transit_gateway_policy_table_id.text or ""
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
