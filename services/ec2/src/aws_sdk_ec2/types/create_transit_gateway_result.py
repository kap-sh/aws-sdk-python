"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway


class CreateTransitGatewayResult(TypedDict):
    transit_gateway: NotRequired["aws_sdk_ec2.types.transit_gateway.TransitGateway"]
    """<p>Information about the transit gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateway" in value:
        import aws_sdk_ec2.types.transit_gateway

        aws_sdk_ec2.types.transit_gateway.serialize_ec2_query(
            value["transit_gateway"], pairs, f"{prefix}.TransitGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayResult:
    out: CreateTransitGatewayResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway = el.find("TransitGateway")
    if child_transit_gateway is not None:
        import aws_sdk_ec2.types.transit_gateway

        out["transit_gateway"] = (
            aws_sdk_ec2.types.transit_gateway.deserialize_ec2_query(
                child_transit_gateway
            )
        )
    return out
