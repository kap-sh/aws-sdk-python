"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesSourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

RuleGroupSourceStatelessRuleMatchAttributesSourcesList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.RuleGroupSourceStatelessRuleMatchAttributesSources"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesSourcesList,
) -> list:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesSourcesList:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

    out: RuleGroupSourceStatelessRuleMatchAttributesSourcesList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.deserialize_json(
                item
            )
        )
    return out
