"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCustomerGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.customer_gateway_list


class DescribeCustomerGatewaysResult(TypedDict, closed=True):
    customer_gateways: NotRequired[
        "capo_ec2.types.customer_gateway_list.CustomerGatewayList"
    ]
    """<p>Information about one or more customer gateways.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCustomerGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "customer_gateways" in value:
        import capo_ec2.types.customer_gateway_list

        capo_ec2.types.customer_gateway_list.serialize_ec2_query(
            value["customer_gateways"], pairs, f"{prefix}.CustomerGatewaySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeCustomerGatewaysResult:
    out: DescribeCustomerGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("CustomerGatewaySet") is not None:
        import capo_ec2.types.customer_gateway_list

        out["customer_gateways"] = (
            capo_ec2.types.customer_gateway_list.deserialize_ec2_query(
                el, "CustomerGatewaySet"
            )
        )
    return out
