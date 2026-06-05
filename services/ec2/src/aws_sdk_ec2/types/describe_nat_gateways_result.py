"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNatGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.nat_gateway_list
    import aws_sdk_ec2.types.string


class DescribeNatGatewaysResult(TypedDict):
    nat_gateways: NotRequired["aws_sdk_ec2.types.nat_gateway_list.NatGatewayList"]
    """<p>Information about the NAT gateways.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNatGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "nat_gateways" in value:
        import aws_sdk_ec2.types.nat_gateway_list

        aws_sdk_ec2.types.nat_gateway_list.serialize_ec2_query(
            value["nat_gateways"], pairs, f"{prefix}.NatGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNatGatewaysResult:
    out: DescribeNatGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("NatGatewaySet") is not None:
        import aws_sdk_ec2.types.nat_gateway_list

        out["nat_gateways"] = aws_sdk_ec2.types.nat_gateway_list.deserialize_ec2_query(
            el, "NatGatewaySet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
