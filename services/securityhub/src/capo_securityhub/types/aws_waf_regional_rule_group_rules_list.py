"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRuleGroupRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_regional_rule_group_rules_details

AwsWafRegionalRuleGroupRulesList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_regional_rule_group_rules_details.AwsWafRegionalRuleGroupRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRuleGroupRulesList) -> list:
    import capo_securityhub.types.aws_waf_regional_rule_group_rules_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_waf_regional_rule_group_rules_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRegionalRuleGroupRulesList:
    import capo_securityhub.types.aws_waf_regional_rule_group_rules_details

    out: AwsWafRegionalRuleGroupRulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_waf_regional_rule_group_rules_details.deserialize_json(
                item
            )
        )
    return out
