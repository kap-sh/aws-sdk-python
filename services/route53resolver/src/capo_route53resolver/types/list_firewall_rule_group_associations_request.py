"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRuleGroupAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_group_association_status
    import capo_route53resolver.types.max_results
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.resource_id


class ListFirewallRuleGroupAssociationsRequest(TypedDict, closed=True):
    firewall_rule_group_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the firewall rule group that you want to retrieve the associations for. Leave this blank to retrieve associations for any rule group. </p>"""
    vpc_id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The unique identifier of the VPC that you want to retrieve the associations for. Leave this blank to retrieve associations for any VPC. </p>"""
    priority: NotRequired["capo_route53resolver.types.priority.Priority"]
    """<p>The setting that determines the processing order of the rule group among the rule groups that are associated with a single VPC. DNS Firewall filters VPC traffic starting from the rule group with the lowest numeric priority setting. </p>"""
    status: NotRequired[
        "capo_route53resolver.types.firewall_rule_group_association_status.FirewallRuleGroupAssociationStatus"
    ]
    """<p>The association <code>Status</code> setting that you want DNS Firewall to filter on for the list. If you don't specify this, then DNS Firewall returns all associations, regardless of status.</p>"""
    max_results: NotRequired["capo_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRuleGroupAssociationsRequest) -> dict:
    out: dict = {}
    if "firewall_rule_group_id" in value:
        out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "status" in value:
        import capo_route53resolver.types.firewall_rule_group_association_status

        out["Status"] = (
            capo_route53resolver.types.firewall_rule_group_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRuleGroupAssociationsRequest:
    out: ListFirewallRuleGroupAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupId" in data:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Status" in data:
        import capo_route53resolver.types.firewall_rule_group_association_status

        out["status"] = (
            capo_route53resolver.types.firewall_rule_group_association_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
