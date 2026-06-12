"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports

RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList: TypeAlias = list[
    "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports.RuleGroupSourceStatelessRuleMatchAttributesSourcePorts"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList,
) -> list:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports

    out: RuleGroupSourceStatelessRuleMatchAttributesSourcePortsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_source_ports.deserialize_json(
                item
            )
        )
    return out
