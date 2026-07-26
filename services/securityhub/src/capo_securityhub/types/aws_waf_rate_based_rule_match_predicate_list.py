"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRateBasedRuleMatchPredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rate_based_rule_match_predicate

AwsWafRateBasedRuleMatchPredicateList: TypeAlias = list[
    "capo_securityhub.types.aws_waf_rate_based_rule_match_predicate.AwsWafRateBasedRuleMatchPredicate"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRateBasedRuleMatchPredicateList) -> list:
    import capo_securityhub.types.aws_waf_rate_based_rule_match_predicate

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_waf_rate_based_rule_match_predicate.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRateBasedRuleMatchPredicateList:
    import capo_securityhub.types.aws_waf_rate_based_rule_match_predicate

    out: AwsWafRateBasedRuleMatchPredicateList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_waf_rate_based_rule_match_predicate.deserialize_json(
                item
            )
        )
    return out
