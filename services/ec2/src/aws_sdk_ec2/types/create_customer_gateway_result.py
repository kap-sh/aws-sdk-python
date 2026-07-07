"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCustomerGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway


class CreateCustomerGatewayResult(TypedDict, closed=True):
    customer_gateway: NotRequired["aws_sdk_ec2.types.customer_gateway.CustomerGateway"]
    """<p>Information about the customer gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCustomerGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "customer_gateway" in value:
        import aws_sdk_ec2.types.customer_gateway

        aws_sdk_ec2.types.customer_gateway.serialize_ec2_query(
            value["customer_gateway"], pairs, f"{prefix}.CustomerGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateCustomerGatewayResult:
    out: CreateCustomerGatewayResult = {}  # type: ignore[typeddict-item]
    child_customer_gateway = el.find("CustomerGateway")
    if child_customer_gateway is not None:
        import aws_sdk_ec2.types.customer_gateway

        out["customer_gateway"] = (
            aws_sdk_ec2.types.customer_gateway.deserialize_ec2_query(
                child_customer_gateway
            )
        )
    return out
