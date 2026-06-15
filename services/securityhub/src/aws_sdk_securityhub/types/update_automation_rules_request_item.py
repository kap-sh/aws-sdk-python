"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateAutomationRulesRequestItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.action_list
    import aws_sdk_securityhub.types.automation_rules_finding_filters
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.rule_order_value
    import aws_sdk_securityhub.types.rule_status


class UpdateAutomationRulesRequestItem(TypedDict):
    rule_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The Amazon Resource Name (ARN) for the rule. </p>"""
    rule_status: NotRequired["aws_sdk_securityhub.types.rule_status.RuleStatus"]
    r"""<p> Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, Security Hub CSPM starts applying the rule to findings and finding updates after the rule is created. To change the value of this parameter after creating a rule, use <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateAutomationRules.html\"> <code>BatchUpdateAutomationRules</code> </a>. </p>"""
    rule_order: NotRequired["aws_sdk_securityhub.types.rule_order_value.RuleOrderValue"]
    """<p> An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub CSPM applies rules with lower values for this parameter first. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the rule. </p>"""
    rule_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the rule. </p>"""
    is_terminal: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub CSPM applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal. </p>"""
    criteria: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_finding_filters.AutomationRulesFindingFilters"
    ]
    """<p> A set of ASFF finding field attributes and corresponding expected values that Security Hub CSPM uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub CSPM applies the rule action to the finding. </p>"""
    actions: NotRequired["aws_sdk_securityhub.types.action_list.ActionList"]
    """<p> One or more actions to update finding fields if a finding matches the conditions specified in <code>Criteria</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomationRulesRequestItem) -> dict:
    out: dict = {}
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "rule_status" in value:
        import aws_sdk_securityhub.types.rule_status

        out["RuleStatus"] = aws_sdk_securityhub.types.rule_status.serialize_json(
            value["rule_status"]
        )
    if "rule_order" in value:
        out["RuleOrder"] = value["rule_order"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "is_terminal" in value:
        out["IsTerminal"] = value["is_terminal"]
    if "criteria" in value:
        import aws_sdk_securityhub.types.automation_rules_finding_filters

        out["Criteria"] = (
            aws_sdk_securityhub.types.automation_rules_finding_filters.serialize_json(
                value["criteria"]
            )
        )
    if "actions" in value:
        import aws_sdk_securityhub.types.action_list

        out["Actions"] = aws_sdk_securityhub.types.action_list.serialize_json(
            value["actions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAutomationRulesRequestItem:
    out: UpdateAutomationRulesRequestItem = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "RuleStatus" in data:
        import aws_sdk_securityhub.types.rule_status

        out["rule_status"] = aws_sdk_securityhub.types.rule_status.deserialize_json(
            data["RuleStatus"]
        )
    if "RuleOrder" in data:
        out["rule_order"] = data["RuleOrder"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "IsTerminal" in data:
        out["is_terminal"] = data["IsTerminal"]
    if "Criteria" in data:
        import aws_sdk_securityhub.types.automation_rules_finding_filters

        out["criteria"] = (
            aws_sdk_securityhub.types.automation_rules_finding_filters.deserialize_json(
                data["Criteria"]
            )
        )
    if "Actions" in data:
        import aws_sdk_securityhub.types.action_list

        out["actions"] = aws_sdk_securityhub.types.action_list.deserialize_json(
            data["Actions"]
        )
    return out
