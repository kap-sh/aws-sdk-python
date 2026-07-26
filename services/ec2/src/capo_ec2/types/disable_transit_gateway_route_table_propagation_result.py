"""Generated from Smithy shape ``com.amazonaws.ec2#DisableTransitGatewayRouteTablePropagationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_propagation


class DisableTransitGatewayRouteTablePropagationResult(TypedDict, closed=True):
    propagation: NotRequired[
        "capo_ec2.types.transit_gateway_propagation.TransitGatewayPropagation"
    ]
    """<p>Information about route propagation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableTransitGatewayRouteTablePropagationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "propagation" in value:
        import capo_ec2.types.transit_gateway_propagation

        capo_ec2.types.transit_gateway_propagation.serialize_ec2_query(
            value["propagation"], pairs, f"{prefix}.Propagation"
        )


def deserialize_ec2_query(
    el: Element,
) -> DisableTransitGatewayRouteTablePropagationResult:
    out: DisableTransitGatewayRouteTablePropagationResult = {}  # type: ignore[typeddict-item]
    child_propagation = el.find("Propagation")
    if child_propagation is not None:
        import capo_ec2.types.transit_gateway_propagation

        out["propagation"] = (
            capo_ec2.types.transit_gateway_propagation.deserialize_ec2_query(
                child_propagation
            )
        )
    return out
