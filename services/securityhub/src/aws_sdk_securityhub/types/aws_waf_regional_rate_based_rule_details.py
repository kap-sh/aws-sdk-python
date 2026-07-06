"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRateBasedRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRateBasedRuleDetails(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the metrics for the rate-based rule.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the rate-based rule.</p>"""
    rate_key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The field that WAF uses to determine whether requests are likely arriving from single source and are subject to rate monitoring.</p>"""
    rate_limit: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The maximum number of requests that have an identical value for the field specified in <code>RateKey</code> that are allowed within a five-minute period. If the number of requests exceeds <code>RateLimit</code> and the other predicates specified in the rule are met, WAF triggers the action for the rule.</p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the rate-based rule.</p>"""
    match_predicates: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list.AwsWafRegionalRateBasedRuleMatchPredicateList"
    ]
    """<p>The predicates to include in the rate-based rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRateBasedRuleDetails) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rate_key" in value:
        out["RateKey"] = value["rate_key"]
    if "rate_limit" in value:
        out["RateLimit"] = value["rate_limit"]
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    if "match_predicates" in value:
        import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list

        out["MatchPredicates"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list.serialize_json(
                value["match_predicates"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafRegionalRateBasedRuleDetails:
    out: AwsWafRegionalRateBasedRuleDetails = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RateKey" in data:
        out["rate_key"] = data["RateKey"]
    if "RateLimit" in data:
        out["rate_limit"] = data["RateLimit"]
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    if "MatchPredicates" in data:
        import aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list

        out["match_predicates"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rate_based_rule_match_predicate_list.deserialize_json(
                data["MatchPredicates"]
            )
        )
    return out
