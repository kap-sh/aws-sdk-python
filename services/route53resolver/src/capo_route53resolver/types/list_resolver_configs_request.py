"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.list_resolver_configs_max_result
    import capo_route53resolver.types.next_token


class ListResolverConfigsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_route53resolver.types.list_resolver_configs_max_result.ListResolverConfigsMaxResult"
    ]
    """<p>The maximum number of Resolver configurations that you want to return in the response to a <code>ListResolverConfigs</code> request. If you don't specify a value for <code>MaxResults</code>, up to 100 Resolver configurations are returned.</p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> Resolver configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListResolverConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverConfigsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverConfigsRequest:
    out: ListResolverConfigsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
