"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCarrierGatewayResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway


class DeleteCarrierGatewayResult(TypedDict):
    carrier_gateway: NotRequired["aws_sdk_ec2.types.carrier_gateway.CarrierGateway"]
    """<p>Information about the carrier gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteCarrierGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "carrier_gateway" in value:
        import aws_sdk_ec2.types.carrier_gateway

        aws_sdk_ec2.types.carrier_gateway.serialize_ec2_query(
            value["carrier_gateway"], pairs, f"{prefix}.CarrierGateway"
        )


def deserialize_ec2_query(el: Element) -> DeleteCarrierGatewayResult:
    out: DeleteCarrierGatewayResult = {}  # type: ignore[typeddict-item]
    child_carrier_gateway = el.find("CarrierGateway")
    if child_carrier_gateway is not None:
        import aws_sdk_ec2.types.carrier_gateway

        out["carrier_gateway"] = (
            aws_sdk_ec2.types.carrier_gateway.deserialize_ec2_query(
                child_carrier_gateway
            )
        )
    return out
