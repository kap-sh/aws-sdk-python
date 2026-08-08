"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCustomerGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.customer_gateway


class CreateCustomerGatewayResult(TypedDict, closed=True):
    customer_gateway: NotRequired["capo_ec2.types.customer_gateway.CustomerGateway"]
    """<p>Information about the customer gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCustomerGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "customer_gateway" in value:
        import capo_ec2.types.customer_gateway

        capo_ec2.types.customer_gateway.serialize_ec2_query(
            value["customer_gateway"], pairs, f"{key_prefix}CustomerGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateCustomerGatewayResult:
    out: CreateCustomerGatewayResult = {}  # type: ignore[typeddict-item]
    child_customer_gateway = el.find("customerGateway")
    if child_customer_gateway is not None:
        import capo_ec2.types.customer_gateway

        out["customer_gateway"] = capo_ec2.types.customer_gateway.deserialize_ec2_query(
            child_customer_gateway
        )
    return out
