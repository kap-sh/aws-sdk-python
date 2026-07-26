"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupRulesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rule_group_rules_action_details
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsWafRuleGroupRulesDetails(TypedDict, closed=True):
    action: NotRequired[
        "capo_securityhub.types.aws_waf_rule_group_rules_action_details.AwsWafRuleGroupRulesActionDetails"
    ]
    """<p>Provides information about what action WAF should take on a web request when it matches the criteria defined in the rule. </p>"""
    priority: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>If you define more than one rule in a web ACL, WAF evaluates each request against the rules in order based on the value of <code>Priority</code>.</p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The rule ID for a rule. </p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupRulesDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_securityhub.types.aws_waf_rule_group_rules_action_details

        out["Action"] = (
            capo_securityhub.types.aws_waf_rule_group_rules_action_details.serialize_json(
                value["action"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafRuleGroupRulesDetails:
    out: AwsWafRuleGroupRulesDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_securityhub.types.aws_waf_rule_group_rules_action_details

        out["action"] = (
            capo_securityhub.types.aws_waf_rule_group_rules_action_details.deserialize_json(
                data["Action"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
