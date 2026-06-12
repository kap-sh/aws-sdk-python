"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRulesAndCustomActionsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_custom_actions_list
    import aws_sdk_securityhub.types.rule_group_source_stateless_rules_list


class RuleGroupSourceStatelessRulesAndCustomActionsDetails(TypedDict):
    custom_actions: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_custom_actions_list.RuleGroupSourceCustomActionsList"
    ]
    """<p>Custom actions for the rule group.</p>"""
    stateless_rules: NotRequired[
        "aws_sdk_securityhub.types.rule_group_source_stateless_rules_list.RuleGroupSourceStatelessRulesList"
    ]
    """<p>Stateless rules for the rule group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRulesAndCustomActionsDetails) -> dict:
    out: dict = {}
    if "custom_actions" in value:
        import aws_sdk_securityhub.types.rule_group_source_custom_actions_list

        out["CustomActions"] = (
            aws_sdk_securityhub.types.rule_group_source_custom_actions_list.serialize_json(
                value["custom_actions"]
            )
        )
    if "stateless_rules" in value:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rules_list

        out["StatelessRules"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rules_list.serialize_json(
                value["stateless_rules"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> RuleGroupSourceStatelessRulesAndCustomActionsDetails:
    out: RuleGroupSourceStatelessRulesAndCustomActionsDetails = {}  # type: ignore[typeddict-item]
    if "CustomActions" in data:
        import aws_sdk_securityhub.types.rule_group_source_custom_actions_list

        out["custom_actions"] = (
            aws_sdk_securityhub.types.rule_group_source_custom_actions_list.deserialize_json(
                data["CustomActions"]
            )
        )
    if "StatelessRules" in data:
        import aws_sdk_securityhub.types.rule_group_source_stateless_rules_list

        out["stateless_rules"] = (
            aws_sdk_securityhub.types.rule_group_source_stateless_rules_list.deserialize_json(
                data["StatelessRules"]
            )
        )
    return out
