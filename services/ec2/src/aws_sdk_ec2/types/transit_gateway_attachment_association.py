"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_association_state


class TransitGatewayAttachmentAssociation(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the route table for the transit gateway.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_association_state.TransitGatewayAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentAssociation,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_route_table_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayRouteTableId",
                str(value["transit_gateway_route_table_id"]),
            )
        )
    if "state" in value:
        import aws_sdk_ec2.types.transit_gateway_association_state

        aws_sdk_ec2.types.transit_gateway_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentAssociation:
    out: TransitGatewayAttachmentAssociation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.transit_gateway_association_state

        out["state"] = (
            aws_sdk_ec2.types.transit_gateway_association_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
