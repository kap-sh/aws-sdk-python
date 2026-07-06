"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverEndpointIpAddressesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip_addresses_response
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token


class ListResolverEndpointIpAddressesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If the specified endpoint has more than <code>MaxResults</code> IP addresses, you can submit another <code>ListResolverEndpointIpAddresses</code> request to get the next group of IP addresses. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The value that you specified for <code>MaxResults</code> in the request.</p>"""
    ip_addresses: NotRequired[
        "aws_sdk_route53resolver.types.ip_addresses_response.IpAddressesResponse"
    ]
    """<p>Information about the IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverEndpointIpAddressesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "ip_addresses" in value:
        import aws_sdk_route53resolver.types.ip_addresses_response

        out["IpAddresses"] = (
            aws_sdk_route53resolver.types.ip_addresses_response.serialize_aws_json_1_1(
                value["ip_addresses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverEndpointIpAddressesResponse:
    out: ListResolverEndpointIpAddressesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "IpAddresses" in data:
        import aws_sdk_route53resolver.types.ip_addresses_response

        out["ip_addresses"] = (
            aws_sdk_route53resolver.types.ip_addresses_response.deserialize_aws_json_1_1(
                data["IpAddresses"]
            )
        )
    return out
