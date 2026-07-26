"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2RulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_rules_details

AwsWafv2RulesList: TypeAlias = list[
    "capo_securityhub.types.aws_wafv2_rules_details.AwsWafv2RulesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2RulesList) -> list:
    import capo_securityhub.types.aws_wafv2_rules_details

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.aws_wafv2_rules_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsWafv2RulesList:
    import capo_securityhub.types.aws_wafv2_rules_details

    out: AwsWafv2RulesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_wafv2_rules_details.deserialize_json(item)
        )
    return out
