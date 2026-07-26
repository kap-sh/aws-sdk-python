"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags

RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags.RuleGroupSourceStatelessRuleMatchAttributesTcpFlags"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList,
) -> list:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags

    out: RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_tcp_flags.deserialize_json(
                item
            )
        )
    return out
