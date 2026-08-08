"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway


class CreateTransitGatewayResult(TypedDict, closed=True):
    transit_gateway: NotRequired["capo_ec2.types.transit_gateway.TransitGateway"]
    """<p>Information about the transit gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway" in value:
        import capo_ec2.types.transit_gateway

        capo_ec2.types.transit_gateway.serialize_ec2_query(
            value["transit_gateway"], pairs, f"{key_prefix}TransitGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayResult:
    out: CreateTransitGatewayResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway = el.find("transitGateway")
    if child_transit_gateway is not None:
        import capo_ec2.types.transit_gateway

        out["transit_gateway"] = capo_ec2.types.transit_gateway.deserialize_ec2_query(
            child_transit_gateway
        )
    return out
