"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafWebAclRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.waf_action
    import aws_sdk_securityhub.types.waf_excluded_rule_list
    import aws_sdk_securityhub.types.waf_override_action


class AwsWafWebAclRule(TypedDict, closed=True):
    action: NotRequired["aws_sdk_securityhub.types.waf_action.WafAction"]
    """<p>Specifies the action that CloudFront or WAF takes when a web request matches the conditions in the rule. </p>"""
    excluded_rules: NotRequired[
        "aws_sdk_securityhub.types.waf_excluded_rule_list.WafExcludedRuleList"
    ]
    """<p>Rules to exclude from a rule group.</p>"""
    override_action: NotRequired[
        "aws_sdk_securityhub.types.waf_override_action.WafOverrideAction"
    ]
    """<p>Use the <code>OverrideAction</code> to test your <code>RuleGroup</code>.</p> <p>Any rule in a <code>RuleGroup</code> can potentially block a request. If you set the <code>OverrideAction</code> to <code>None</code>, the <code>RuleGroup</code> blocks a request if any individual rule in the <code>RuleGroup</code> matches the request and is configured to block that request.</p> <p>However, if you first want to test the <code>RuleGroup</code>, set the <code>OverrideAction</code> to <code>Count</code>. The <code>RuleGroup</code> then overrides any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests are counted.</p> <p> <code>ActivatedRule</code>|<code>OverrideAction</code> applies only when updating or adding a <code>RuleGroup</code> to a web ACL. In this case you don't use <code>ActivatedRule</code> <code>Action</code>. For all other update requests, <code>ActivatedRule</code> <code>Action</code> is used instead of <code>ActivatedRule</code> <code>OverrideAction</code>.</p>"""
    priority: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>Specifies the order in which the rules in a web ACL are evaluated. Rules with a lower value for <code>Priority</code> are evaluated before rules with a higher value. The value must be a unique integer. If you add multiple rules to a web ACL, the values don't need to be consecutive.</p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier for a rule.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The rule type.</p> <p>Valid values: <code>REGULAR</code> | <code>RATE_BASED</code> | <code>GROUP</code> </p> <p>The default is <code>REGULAR</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafWebAclRule) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_securityhub.types.waf_action

        out["Action"] = aws_sdk_securityhub.types.waf_action.serialize_json(
            value["action"]
        )
    if "excluded_rules" in value:
        import aws_sdk_securityhub.types.waf_excluded_rule_list

        out["ExcludedRules"] = (
            aws_sdk_securityhub.types.waf_excluded_rule_list.serialize_json(
                value["excluded_rules"]
            )
        )
    if "override_action" in value:
        import aws_sdk_securityhub.types.waf_override_action

        out["OverrideAction"] = (
            aws_sdk_securityhub.types.waf_override_action.serialize_json(
                value["override_action"]
            )
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsWafWebAclRule:
    out: AwsWafWebAclRule = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_securityhub.types.waf_action

        out["action"] = aws_sdk_securityhub.types.waf_action.deserialize_json(
            data["Action"]
        )
    if "ExcludedRules" in data:
        import aws_sdk_securityhub.types.waf_excluded_rule_list

        out["excluded_rules"] = (
            aws_sdk_securityhub.types.waf_excluded_rule_list.deserialize_json(
                data["ExcludedRules"]
            )
        )
    if "OverrideAction" in data:
        import aws_sdk_securityhub.types.waf_override_action

        out["override_action"] = (
            aws_sdk_securityhub.types.waf_override_action.deserialize_json(
                data["OverrideAction"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
