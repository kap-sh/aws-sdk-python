"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_association


class AssociateTransitGatewayRouteTableResult(TypedDict, closed=True):
    association: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_association.TransitGatewayAssociation"
    ]
    """<p>The ID of the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTransitGatewayRouteTableResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "association" in value:
        import aws_sdk_ec2.types.transit_gateway_association

        aws_sdk_ec2.types.transit_gateway_association.serialize_ec2_query(
            value["association"], pairs, f"{prefix}.Association"
        )


def deserialize_ec2_query(el: Element) -> AssociateTransitGatewayRouteTableResult:
    out: AssociateTransitGatewayRouteTableResult = {}  # type: ignore[typeddict-item]
    child_association = el.find("Association")
    if child_association is not None:
        import aws_sdk_ec2.types.transit_gateway_association

        out["association"] = (
            aws_sdk_ec2.types.transit_gateway_association.deserialize_ec2_query(
                child_association
            )
        )
    return out
