"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverDnssecConfigsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.filters
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token


class ListResolverDnssecConfigsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p> <i>Optional</i>: An integer that specifies the maximum number of DNSSEC configuration results that you want Amazon Route 53 to return. If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 100 configuration per page.</p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> DNSSEC configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListResolverDnssecConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>"""
    filters: NotRequired["aws_sdk_route53resolver.types.filters.Filters"]
    """<p>An optional specification to return a subset of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverDnssecConfigsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_route53resolver.types.filters

        out["Filters"] = aws_sdk_route53resolver.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverDnssecConfigsRequest:
    out: ListResolverDnssecConfigsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_route53resolver.types.filters

        out["filters"] = aws_sdk_route53resolver.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
