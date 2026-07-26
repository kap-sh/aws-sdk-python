"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateAutomationRuleV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_list_v2
    import capo_securityhub.types.criteria
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.rule_order_value_v2
    import capo_securityhub.types.rule_status_v2


class UpdateAutomationRuleV2Request(TypedDict, closed=True):
    identifier: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the automation rule.</p>"""
    rule_status: NotRequired["capo_securityhub.types.rule_status_v2.RuleStatusV2"]
    """<p>The status of the automation rule.</p>"""
    rule_order: NotRequired[
        "capo_securityhub.types.rule_order_value_v2.RuleOrderValueV2"
    ]
    """<p>Represents a value for the rule priority.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the automation rule.</p>"""
    rule_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the automation rule.</p>"""
    criteria: NotRequired["capo_securityhub.types.criteria.Criteria"]
    """<p>The filtering type and configuration of the automation rule.</p>"""
    actions: NotRequired[
        "capo_securityhub.types.automation_rules_action_list_v2.AutomationRulesActionListV2"
    ]
    """<p>A list of actions to be performed when the rule criteria is met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomationRuleV2Request) -> dict:
    out: dict = {}
    if "rule_status" in value:
        import capo_securityhub.types.rule_status_v2

        out["RuleStatus"] = capo_securityhub.types.rule_status_v2.serialize_json(
            value["rule_status"]
        )
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "criteria" in value:
        import capo_securityhub.types.criteria

        out["Criteria"] = capo_securityhub.types.criteria.serialize_json(
            value["criteria"]
        )
    if "actions" in value:
        import capo_securityhub.types.automation_rules_action_list_v2

        out["Actions"] = (
            capo_securityhub.types.automation_rules_action_list_v2.serialize_json(
                value["actions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAutomationRuleV2Request:
    out: UpdateAutomationRuleV2Request = {}  # type: ignore[typeddict-item]
    if "RuleStatus" in data:
        import capo_securityhub.types.rule_status_v2

        out["rule_status"] = capo_securityhub.types.rule_status_v2.deserialize_json(
            data["RuleStatus"]
        )
    if "RuleOrder" in data:
        out["rule_order"] = data["RuleOrder"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "Criteria" in data:
        import capo_securityhub.types.criteria

        out["criteria"] = capo_securityhub.types.criteria.deserialize_json(
            data["Criteria"]
        )
    if "Actions" in data:
        import capo_securityhub.types.automation_rules_action_list_v2

        out["actions"] = (
            capo_securityhub.types.automation_rules_action_list_v2.deserialize_json(
                data["Actions"]
            )
        )
    return out
