"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverRuleAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.resolver_rule_associations


class ListResolverRuleAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If more than <code>MaxResults</code> rule associations match the specified criteria, you can submit another <code>ListResolverRuleAssociation</code> request to get the next group of results. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The value that you specified for <code>MaxResults</code> in the request.</p>"""
    resolver_rule_associations: NotRequired[
        "aws_sdk_route53resolver.types.resolver_rule_associations.ResolverRuleAssociations"
    ]
    """<p>The associations that were created between Resolver rules and VPCs using the current Amazon Web Services account, and that match the specified filters, if any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverRuleAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resolver_rule_associations" in value:
        import aws_sdk_route53resolver.types.resolver_rule_associations

        out["ResolverRuleAssociations"] = (
            aws_sdk_route53resolver.types.resolver_rule_associations.serialize_aws_json_1_1(
                value["resolver_rule_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverRuleAssociationsResponse:
    out: ListResolverRuleAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResolverRuleAssociations" in data:
        import aws_sdk_route53resolver.types.resolver_rule_associations

        out["resolver_rule_associations"] = (
            aws_sdk_route53resolver.types.resolver_rule_associations.deserialize_aws_json_1_1(
                data["ResolverRuleAssociations"]
            )
        )
    return out
