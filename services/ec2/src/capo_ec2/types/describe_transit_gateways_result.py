"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_list


class DescribeTransitGatewaysResult(TypedDict, closed=True):
    transit_gateways: NotRequired[
        "capo_ec2.types.transit_gateway_list.TransitGatewayList"
    ]
    """<p>Information about the transit gateways.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateways" in value:
        import capo_ec2.types.transit_gateway_list

        capo_ec2.types.transit_gateway_list.serialize_ec2_query(
            value["transit_gateways"], pairs, f"{key_prefix}TransitGatewaySet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewaysResult:
    out: DescribeTransitGatewaysResult = {}  # type: ignore[typeddict-item]
    child_transit_gateways = el.find("transitGatewaySet")
    if child_transit_gateways is not None:
        import capo_ec2.types.transit_gateway_list

        out["transit_gateways"] = (
            capo_ec2.types.transit_gateway_list.deserialize_ec2_query(
                child_transit_gateways
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
