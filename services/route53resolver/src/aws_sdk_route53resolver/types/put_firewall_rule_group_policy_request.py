"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutFirewallRuleGroupPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn
    import aws_sdk_route53resolver.types.firewall_rule_group_policy


class PutFirewallRuleGroupPolicyRequest(TypedDict):
    arn: "aws_sdk_route53resolver.types.arn.Arn"
    """<p>The ARN (Amazon Resource Name) for the rule group that you want to share.</p>"""
    firewall_rule_group_policy: "aws_sdk_route53resolver.types.firewall_rule_group_policy.FirewallRuleGroupPolicy"
    """<p>The Identity and Access Management (Amazon Web Services IAM) policy to attach to the rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFirewallRuleGroupPolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FirewallRuleGroupPolicy"] = value["firewall_rule_group_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFirewallRuleGroupPolicyRequest:
    out: PutFirewallRuleGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PutFirewallRuleGroupPolicyRequest.arn required")
    if "FirewallRuleGroupPolicy" in data:
        out["firewall_rule_group_policy"] = data["FirewallRuleGroupPolicy"]
    else:
        raise DeserializationError(
            "PutFirewallRuleGroupPolicyRequest.firewall_rule_group_policy required"
        )
    return out
