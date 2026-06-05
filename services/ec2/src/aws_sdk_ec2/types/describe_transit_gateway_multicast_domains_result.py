"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayMulticastDomainsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_list


class DescribeTransitGatewayMulticastDomainsResult(TypedDict):
    transit_gateway_multicast_domains: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_list.TransitGatewayMulticastDomainList"
    ]
    """<p>Information about the transit gateway multicast domains.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayMulticastDomainsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_multicast_domains" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_list

        aws_sdk_ec2.types.transit_gateway_multicast_domain_list.serialize_ec2_query(
            value["transit_gateway_multicast_domains"],
            pairs,
            f"{prefix}.TransitGatewayMulticastDomains",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayMulticastDomainsResult:
    out: DescribeTransitGatewayMulticastDomainsResult = {}  # type: ignore[typeddict-item]
    if el.find("TransitGatewayMulticastDomains") is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_list

        out["transit_gateway_multicast_domains"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_domain_list.deserialize_ec2_query(
                el, "TransitGatewayMulticastDomains"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
