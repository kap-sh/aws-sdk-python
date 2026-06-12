"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.resolver_rules


class ListResolverRulesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> Resolver rules match the specified criteria, you can submit another <code>ListResolverRules</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The value that you specified for <code>MaxResults</code> in the request.</p>"""
    resolver_rules: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rules.ResolverRules"
    ]
    """<p>The Resolver rules that were created using the current Amazon Web Services account and that match the specified filters, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resolver_rules" in value:
        import aws_sdk_route53resolver.types.resolver_rules

        out["ResolverRules"] = (
            aws_sdk_route53resolver.types.resolver_rules.serialize_aws_json_1_1(
                value["resolver_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverRulesResponse:
    out: ListResolverRulesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResolverRules" in data:
        import aws_sdk_route53resolver.types.resolver_rules

        out["resolver_rules"] = (
            aws_sdk_route53resolver.types.resolver_rules.deserialize_aws_json_1_1(
                data["ResolverRules"]
            )
        )
    return out
