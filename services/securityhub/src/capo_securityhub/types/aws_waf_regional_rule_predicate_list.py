"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRulePredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_regional_rule_predicate_list_details

AwsWafRegionalRulePredicateList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_regional_rule_predicate_list_details.AwsWafRegionalRulePredicateListDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRulePredicateList) -> list:
    import capo_securityhub.types.aws_waf_regional_rule_predicate_list_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_waf_regional_rule_predicate_list_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRegionalRulePredicateList:
    import capo_securityhub.types.aws_waf_regional_rule_predicate_list_details

    out: AwsWafRegionalRulePredicateList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_waf_regional_rule_predicate_list_details.deserialize_json(
                item
            )
        )
    return out
