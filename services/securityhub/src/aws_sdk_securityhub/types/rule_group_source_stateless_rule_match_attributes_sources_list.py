"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleGroupSourceStatelessRuleMatchAttributesSourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

RuleGroupSourceStatelessRuleMatchAttributesSourcesList: TypeAlias = list[
    "aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.RuleGroupSourceStatelessRuleMatchAttributesSources"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: RuleGroupSourceStatelessRuleMatchAttributesSourcesList,
) -> list:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> RuleGroupSourceStatelessRuleMatchAttributesSourcesList:
    import aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources

    out: RuleGroupSourceStatelessRuleMatchAttributesSourcesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.rule_group_source_stateless_rule_match_attributes_sources.deserialize_json(
                item
            )
        )
    return out
