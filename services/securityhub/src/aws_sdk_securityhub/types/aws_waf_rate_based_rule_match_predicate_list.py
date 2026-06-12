"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRateBasedRuleMatchPredicateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate

AwsWafRateBasedRuleMatchPredicateList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate.AwsWafRateBasedRuleMatchPredicate"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRateBasedRuleMatchPredicateList) -> list:
    import aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsWafRateBasedRuleMatchPredicateList:
    import aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate

    out: AwsWafRateBasedRuleMatchPredicateList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_waf_rate_based_rule_match_predicate.deserialize_json(
                item
            )
        )
    return out
