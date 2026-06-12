"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesDestinationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations

RuleGroupSourceStatelessRuleMatchAttributesDestinationsList: TypeAlias = list[
    "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations.RuleGroupSourceStatelessRuleMatchAttributesDestinations"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesDestinationsList,
) -> list:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesDestinationsList:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations

    out: RuleGroupSourceStatelessRuleMatchAttributesDestinationsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_destinations.deserialize_json(
                item
            )
        )
    return out
