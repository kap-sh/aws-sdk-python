"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_waf_rule_predicate_list
    import capo_securityhub.types.non_empty_string


class AwsWafRuleDetails(TypedDict, closed=True):
    metric_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the metrics for this rule. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A descriptive name for the rule. </p>"""
    predicate_list: NotRequired[
        "capo_securityhub.types.aws_waf_rule_predicate_list.AwsWafRulePredicateList"
    ]
    """<p>Specifies the <code>ByteMatchSet</code>, <code>IPSet</code>, <code>SqlInjectionMatchSet</code>, <code>XssMatchSet</code>, <code>RegexMatchSet</code>, <code>GeoMatchSet</code>, and <code>SizeConstraintSet</code> objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings. </p>"""
    rule_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the WAF rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleDetails) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "predicate_list" in value:
        import capo_securityhub.types.aws_waf_rule_predicate_list

        out["PredicateList"] = (
            capo_securityhub.types.aws_waf_rule_predicate_list.serialize_json(
                value["predicate_list"]
            )
        )
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> AwsWafRuleDetails:
    out: AwsWafRuleDetails = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PredicateList" in data:
        import capo_securityhub.types.aws_waf_rule_predicate_list

        out["predicate_list"] = (
            capo_securityhub.types.aws_waf_rule_predicate_list.deserialize_json(
                data["PredicateList"]
            )
        )
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    return out
