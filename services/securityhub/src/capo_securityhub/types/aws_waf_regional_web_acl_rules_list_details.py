"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalWebAclRulesListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details
    import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsWafRegionalWebAclRulesListDetails(TypedDict, closed=True):
    action: NotRequired[
        "capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details.AwsWafRegionalWebAclRulesListActionDetails"
    ]
    """<p>The action that WAF takes when a web request matches all conditions in the rule, such as allow, block, or count the request. </p>"""
    override_action: NotRequired[
        "capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details.AwsWafRegionalWebAclRulesListOverrideActionDetails"
    ]
    """<p>Overrides the rule evaluation result in the rule group. </p>"""
    priority: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The order in which WAF evaluates the rules in a web ACL. </p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of an WAF Regional rule to associate with a web ACL. </p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>For actions that are associated with a rule, the action that WAF takes when a web request matches all conditions in a rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalWebAclRulesListDetails) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details

        out["Action"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details.serialize_json(
                value["action"]
            )
        )
    if "override_action" in value:
        import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details

        out["OverrideAction"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details.serialize_json(
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


def deserialize_json(data: dict) -> AwsWafRegionalWebAclRulesListDetails:
    out: AwsWafRegionalWebAclRulesListDetails = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details

        out["action"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_rules_list_action_details.deserialize_json(
                data["Action"]
            )
        )
    if "OverrideAction" in data:
        import capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details

        out["override_action"] = (
            capo_securityhub.types.aws_waf_regional_web_acl_rules_list_override_action_details.deserialize_json(
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
