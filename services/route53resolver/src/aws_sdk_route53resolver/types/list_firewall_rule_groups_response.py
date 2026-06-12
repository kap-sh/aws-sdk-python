"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRuleGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_metadata_list
    import aws_sdk_route53resolver.types.next_token


class ListFirewallRuleGroupsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    firewall_rule_groups: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_metadata_list.FirewallRuleGroupMetadataList"
    ]
    """<p>A list of your firewall rule groups.</p> <p>This might be a partial list of the rule groups that you have defined. For information, see <code>MaxResults</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_rule_groups" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group_metadata_list

        out["FirewallRuleGroups"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_metadata_list.serialize_aws_json_1_1(
                value["firewall_rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRuleGroupsResponse:
    out: ListFirewallRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FirewallRuleGroups" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group_metadata_list

        out["firewall_rule_groups"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_metadata_list.deserialize_aws_json_1_1(
                data["FirewallRuleGroups"]
            )
        )
    return out
