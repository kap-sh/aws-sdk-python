"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRulePredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rule_predicate_list_details

AwsWafRulePredicateList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_rule_predicate_list_details.AwsWafRulePredicateListDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRulePredicateList) -> list:
    import capo_securityhub.types.aws_waf_rule_predicate_list_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_waf_rule_predicate_list_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRulePredicateList:
    import capo_securityhub.types.aws_waf_rule_predicate_list_details

    out: AwsWafRulePredicateList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_waf_rule_predicate_list_details.deserialize_json(
                item
            )
        )
    return out
