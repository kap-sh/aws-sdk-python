"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCarrierGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.carrier_gateway


class CreateCarrierGatewayResult(TypedDict, closed=True):
    carrier_gateway: NotRequired["capo_ec2.types.carrier_gateway.CarrierGateway"]
    """<p>Information about the carrier gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCarrierGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "carrier_gateway" in value:
        import capo_ec2.types.carrier_gateway

        capo_ec2.types.carrier_gateway.serialize_ec2_query(
            value["carrier_gateway"], pairs, f"{key_prefix}CarrierGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateCarrierGatewayResult:
    out: CreateCarrierGatewayResult = {}  # type: ignore[typeddict-item]
    child_carrier_gateway = el.find("carrierGateway")
    if child_carrier_gateway is not None:
        import capo_ec2.types.carrier_gateway

        out["carrier_gateway"] = capo_ec2.types.carrier_gateway.deserialize_ec2_query(
            child_carrier_gateway
        )
    return out
