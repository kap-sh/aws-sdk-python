"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRegionalRuleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRegionalRuleDetails(TypedDict, closed=True):
    metric_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A name for the metrics for the rule. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A descriptive name for the rule. </p>"""
    predicate_list: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list.AwsWafRegionalRulePredicateList"
    ]
    """<p>Specifies the <code>ByteMatchSet</code>, <code>IPSet</code>, <code>SqlInjectionMatchSet</code>, <code>XssMatchSet</code>, <code>RegexMatchSet</code>, <code>GeoMatchSet</code>, and <code>SizeConstraintSet</code> objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings. </p>"""
    rule_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the rule. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRegionalRuleDetails) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "predicate_list" in value:
        import aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list

        out["PredicateList"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list.serialize_json(
                value["predicate_list"]
            )
        )
    if "rule_id" in value:
        out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> AwsWafRegionalRuleDetails:
    out: AwsWafRegionalRuleDetails = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "PredicateList" in data:
        import aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list

        out["predicate_list"] = (
            aws_sdk_securityhub.types.aws_waf_regional_rule_predicate_list.deserialize_json(
                data["PredicateList"]
            )
        )
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    return out
