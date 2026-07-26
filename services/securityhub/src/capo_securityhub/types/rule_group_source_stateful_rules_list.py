"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatefulRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_stateful_rules_details

RuleGroupSourceStatefulRulesList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_stateful_rules_details.RuleGroupSourceStatefulRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleGroupSourceStatefulRulesList) -> list:
    import capo_securityhub.types.rule_group_source_stateful_rules_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_stateful_rules_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RuleGroupSourceStatefulRulesList:
    import capo_securityhub.types.rule_group_source_stateful_rules_details

    out: RuleGroupSourceStatefulRulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_stateful_rules_details.deserialize_json(
                item
            )
        )
    return out
