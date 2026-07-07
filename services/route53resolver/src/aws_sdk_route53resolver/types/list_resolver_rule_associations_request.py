"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverRuleAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.filters
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token


class ListResolverRuleAssociationsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of rule associations that you want to return in the response to a <code>ListResolverRuleAssociations</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 rule associations. </p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>For the first <code>ListResolverRuleAssociation</code> request, omit this value.</p> <p>If you have more than <code>MaxResults</code> rule associations, you can submit another <code>ListResolverRuleAssociation</code> request to get the next group of rule associations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    filters: NotRequired["aws_sdk_route53resolver.types.filters.Filters"]
    """<p>An optional specification to return a subset of Resolver rules, such as Resolver rules that are associated with the same VPC ID.</p> <note> <p>If you submit a second or subsequent <code>ListResolverRuleAssociations</code> request and specify the <code>NextToken</code> parameter, you must use the same values for <code>Filters</code>, if any, as in the previous request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverRuleAssociationsRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListResolverRuleAssociationsRequest:
    out: ListResolverRuleAssociationsRequest = {}  # type: ignore[typeddict-item]
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
