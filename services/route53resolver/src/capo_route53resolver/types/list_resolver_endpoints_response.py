"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.max_results
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.resolver_endpoints


class ListResolverEndpointsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> IP addresses match the specified criteria, you can submit another <code>ListResolverEndpoint</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    max_results: NotRequired["capo_route53resolver.types.max_results.MaxResults"]
    """<p>The value that you specified for <code>MaxResults</code> in the request.</p>"""
    resolver_endpoints: NotRequired[
        "capo_route53resolver.types.resolver_endpoints.ResolverEndpoints"
    ]
    """<p>The Resolver endpoints that were created by using the current Amazon Web Services account, and that match the specified filters, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverEndpointsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resolver_endpoints" in value:
        import capo_route53resolver.types.resolver_endpoints

        out["ResolverEndpoints"] = (
            capo_route53resolver.types.resolver_endpoints.serialize_aws_json_1_1(
                value["resolver_endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverEndpointsResponse:
    out: ListResolverEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResolverEndpoints" in data:
        import capo_route53resolver.types.resolver_endpoints

        out["resolver_endpoints"] = (
            capo_route53resolver.types.resolver_endpoints.deserialize_aws_json_1_1(
                data["ResolverEndpoints"]
            )
        )
    return out
