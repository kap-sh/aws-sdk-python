"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rule_group_rules_details

AwsWafRuleGroupRulesList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_rule_group_rules_details.AwsWafRuleGroupRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupRulesList) -> list:
    import capo_securityhub.types.aws_waf_rule_group_rules_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_waf_rule_group_rules_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsWafRuleGroupRulesList:
    import capo_securityhub.types.aws_waf_rule_group_rules_details

    out: AwsWafRuleGroupRulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_waf_rule_group_rules_details.deserialize_json(
                item
            )
        )
    return out
