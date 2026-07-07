"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.action
    import aws_sdk_route53resolver.types.max_results
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.priority
    import aws_sdk_route53resolver.types.resource_id


class ListFirewallRulesRequest(TypedDict, closed=True):
    firewall_rule_group_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group that you want to retrieve the rules for. </p>"""
    priority: NotRequired["aws_sdk_route53resolver.types.priority.Priority"]
    """<p>Optional additional filter for the rules to retrieve.</p> <p>The setting that determines the processing order of the rules in a rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>"""
    action: NotRequired["aws_sdk_route53resolver.types.action.Action"]
    """<p>Optional additional filter for the rules to retrieve.</p> <p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through. Not availabe for DNS Firewall Advanced rules.</p> </li> <li> <p> <code>ALERT</code> - Permit the request to go through but send an alert to the logs.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. If this is specified, additional handling details are provided in the rule's <code>BlockResponse</code> setting. </p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>"""
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRulesRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "action" in value:
        import aws_sdk_route53resolver.types.action

        out["Action"] = aws_sdk_route53resolver.types.action.serialize_aws_json_1_1(
            value["action"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRulesRequest:
    out: ListFirewallRulesRequest = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupId" in data:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        raise DeserializationError(
            "ListFirewallRulesRequest.firewall_rule_group_id required"
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Action" in data:
        import aws_sdk_route53resolver.types.action

        out["action"] = aws_sdk_route53resolver.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
