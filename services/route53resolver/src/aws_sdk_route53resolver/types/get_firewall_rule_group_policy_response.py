"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallRuleGroupPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_policy


class GetFirewallRuleGroupPolicyResponse(TypedDict, closed=True):
    firewall_rule_group_policy: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_policy.FirewallRuleGroupPolicy"
    ]
    """<p>The Identity and Access Management (Amazon Web Services IAM) policy for sharing the specified rule group. You can use the policy to share the rule group using Resource Access Manager (RAM). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallRuleGroupPolicyResponse) -> dict:
    out: dict = {}
    if "firewall_rule_group_policy" in value:
        out["FirewallRuleGroupPolicy"] = value["firewall_rule_group_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallRuleGroupPolicyResponse:
    out: GetFirewallRuleGroupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupPolicy" in data:
        out["firewall_rule_group_policy"] = data["FirewallRuleGroupPolicy"]
    return out
