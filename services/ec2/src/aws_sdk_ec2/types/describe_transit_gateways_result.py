"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_list


class DescribeTransitGatewaysResult(TypedDict):
    transit_gateways: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_list.TransitGatewayList"
    ]
    """<p>Information about the transit gateways.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "transit_gateways" in value:
        import aws_sdk_ec2.types.transit_gateway_list

        aws_sdk_ec2.types.transit_gateway_list.serialize_ec2_query(
            value["transit_gateways"], pairs, f"{prefix}.TransitGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewaysResult:
    out: DescribeTransitGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewaySet") is not None:
        import aws_sdk_ec2.types.transit_gateway_list

        out["transit_gateways"] = (
            aws_sdk_ec2.types.transit_gateway_list.deserialize_ec2_query(
                el, "TransitGatewaySet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
