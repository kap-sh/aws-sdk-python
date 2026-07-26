"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRuleTypesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.max_results
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.rule_type_name


class ListFirewallRuleTypesRequest(TypedDict, closed=True):
    rule_type: NotRequired["capo_route53resolver.types.rule_type_name.RuleTypeName"]
    """<p>The rule type to filter by. If specified, only rule types matching this value are returned.</p>"""
    max_results: NotRequired["capo_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>For the first call to this list request, omit this value. When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver provides a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRuleTypesRequest) -> dict:
    out: dict = {}
    if "rule_type" in value:
        out["RuleType"] = value["rule_type"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRuleTypesRequest:
    out: ListFirewallRuleTypesRequest = {}  # type: ignore[typeddict-item]
    if "RuleType" in data:
        out["rule_type"] = data["RuleType"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
