"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCarrierGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.carrier_gateway_set
    import capo_ec2.types.string


class DescribeCarrierGatewaysResult(TypedDict, closed=True):
    carrier_gateways: NotRequired[
        "capo_ec2.types.carrier_gateway_set.CarrierGatewaySet"
    ]
    """<p>Information about the carrier gateway.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCarrierGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "carrier_gateways" in value:
        import capo_ec2.types.carrier_gateway_set

        capo_ec2.types.carrier_gateway_set.serialize_ec2_query(
            value["carrier_gateways"], pairs, f"{prefix}.CarrierGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeCarrierGatewaysResult:
    out: DescribeCarrierGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("CarrierGatewaySet") is not None:
        import capo_ec2.types.carrier_gateway_set

        out["carrier_gateways"] = (
            capo_ec2.types.carrier_gateway_set.deserialize_ec2_query(
                el, "CarrierGatewaySet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
