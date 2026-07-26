"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_stateless_rules_details

RuleGroupSourceStatelessRulesList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_stateless_rules_details.RuleGroupSourceStatelessRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatelessRulesList) -> list:
    import capo_securityhub.types.rule_group_source_stateless_rules_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rules_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RuleGroupSourceStatelessRulesList:
    import capo_securityhub.types.rule_group_source_stateless_rules_details

    out: RuleGroupSourceStatelessRulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rules_details.deserialize_json(
                item
            )
        )
    return out
