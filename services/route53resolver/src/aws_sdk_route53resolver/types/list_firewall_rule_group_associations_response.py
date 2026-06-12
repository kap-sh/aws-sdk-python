"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRuleGroupAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_associations
    import aws_sdk_route53resolver.types.next_token


class ListFirewallRuleGroupAssociationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    firewall_rule_group_associations: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_associations.FirewallRuleGroupAssociations"
    ]
    """<p>A list of your firewall rule group associations.</p> <p>This might be a partial list of the associations that you have defined. For information, see <code>MaxResults</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRuleGroupAssociationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_rule_group_associations" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group_associations

        out["FirewallRuleGroupAssociations"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_associations.serialize_aws_json_1_1(
                value["firewall_rule_group_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRuleGroupAssociationsResponse:
    out: ListFirewallRuleGroupAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FirewallRuleGroupAssociations" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group_associations

        out["firewall_rule_group_associations"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_associations.deserialize_aws_json_1_1(
                data["FirewallRuleGroupAssociations"]
            )
        )
    return out
