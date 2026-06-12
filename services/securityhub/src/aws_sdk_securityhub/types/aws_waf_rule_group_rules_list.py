"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_rule_group_rules_details

AwsWafRuleGroupRulesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_waf_rule_group_rules_details.AwsWafRuleGroupRulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupRulesList) -> list:
    import aws_sdk_securityhub.types.aws_waf_rule_group_rules_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_waf_rule_group_rules_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRuleGroupRulesList:
    import aws_sdk_securityhub.types.aws_waf_rule_group_rules_details

    out: AwsWafRuleGroupRulesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_waf_rule_group_rules_details.deserialize_json(
                item
            )
        )
    return out
