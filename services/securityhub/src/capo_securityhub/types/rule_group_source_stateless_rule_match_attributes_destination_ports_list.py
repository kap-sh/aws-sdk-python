"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports

RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList: TypeAlias = list[
    "capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports.RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList,
) -> list:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList:
    import capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports

    out: RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsList = []
    for item in data:
        out.append(
            capo_securityhub.types.rule_group_source_stateless_rule_match_attributes_destination_ports.deserialize_json(
                item
            )
        )
    return out
