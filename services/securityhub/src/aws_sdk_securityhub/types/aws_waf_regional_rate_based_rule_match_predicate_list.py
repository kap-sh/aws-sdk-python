"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRateBasedRuleMatchPredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate

AwsWafRegionalRateBasedRuleMatchPredicateList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate.AwsWafRegionalRateBasedRuleMatchPredicate"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRateBasedRuleMatchPredicateList) -> list:
    import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRegionalRateBasedRuleMatchPredicateList:
    import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate

    out: AwsWafRegionalRateBasedRuleMatchPredicateList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate.deserialize_json(
                item
            )
        )
    return out
