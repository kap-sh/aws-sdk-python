"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_association


class DisassociateTransitGatewayRouteTableResult(TypedDict, closed=True):
    association: NotRequired[
        "capo_ec2.types.transit_gateway_association.TransitGatewayAssociation"
    ]
    """<p>Information about the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateTransitGatewayRouteTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association" in value:
        import capo_ec2.types.transit_gateway_association

        capo_ec2.types.transit_gateway_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )


def deserialize_ec2_query(el: Element) -> DisassociateTransitGatewayRouteTableResult:
    out: DisassociateTransitGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import capo_ec2.types.transit_gateway_association

        out["association"] = (
            capo_ec2.types.transit_gateway_association.deserialize_ec2_query(
                child_association
            )
        )
    return out
