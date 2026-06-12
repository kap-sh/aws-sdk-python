"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRuleGroupRulesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRuleGroupRulesDetails(TypedDict):
    action: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details.AwsWafRegionalRuleGroupRulesActionDetails"
    ]
    """<p>The action that WAF should take on a web request when it matches the criteria defined in the rule. </p>"""
    priority: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>If you define more than one rule in a web ACL, WAF evaluates each request against the rules in order based on the value of <code>Priority</code>. </p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID for a rule. </p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of rule in the rule group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRuleGroupRulesDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details

        out["Action"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details.serialize_json(
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


def deserialize_json(data: dict) -> AwsWafRegionalRuleGroupRulesDetails:
    out: AwsWafRegionalRuleGroupRulesDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details

        out["action"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rule_group_rules_action_details.deserialize_json(
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
