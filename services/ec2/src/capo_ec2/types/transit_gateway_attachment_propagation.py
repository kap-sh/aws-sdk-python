"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentPropagation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_propagation_state


class TransitGatewayAttachmentPropagation(TypedDict, closed=True):
    transit_gateway_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the propagation route table.</p>"""
    state: NotRequired[
        "capo_ec2.types.transit_gateway_propagation_state.TransitGatewayPropagationState"
    ]
    """<p>The state of the propagation route table.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentPropagation,
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
    if "state" in value:
        import capo_ec2.types.transit_gateway_propagation_state

        capo_ec2.types.transit_gateway_propagation_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentPropagation:
    out: TransitGatewayAttachmentPropagation = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_table_id = el.find("TransitGatewayRouteTableId")
    if child_transit_gateway_route_table_id is not None:
        out["transit_gateway_route_table_id"] = str(
            child_transit_gateway_route_table_id.text or ""
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.transit_gateway_propagation_state

        out["state"] = (
            capo_ec2.types.transit_gateway_propagation_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
