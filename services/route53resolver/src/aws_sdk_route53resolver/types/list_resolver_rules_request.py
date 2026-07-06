"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.filters
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token


class ListResolverRulesRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of Resolver rules that you want to return in the response to a <code>ListResolverRules</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 Resolver rules.</p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>For the first <code>ListResolverRules</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> Resolver rules, you can submit another <code>ListResolverRules</code> request to get the next group of Resolver rules. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    filters: NotRequired["aws_sdk_route53resolver.types.filters.Filters"]
    """<p>An optional specification to return a subset of Resolver rules, such as all Resolver rules that are associated with the same Resolver endpoint.</p> <note> <p>If you submit a second or subsequent <code>ListResolverRules</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverRulesRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListResolverRulesRequest:
    out: ListResolverRulesRequest = {}  # type: ignore[typeddict-item]
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
