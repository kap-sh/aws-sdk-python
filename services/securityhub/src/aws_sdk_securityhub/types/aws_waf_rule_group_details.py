"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafRuleGroupDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_waf_rule_group_rules_list
    import aws_sdk_securityhub.types.non_empty_string


class AwsWafRuleGroupDetails(TypedDict):
    metric_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the metrics for this rule group. </p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the rule group. </p>"""
    rule_group_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the rule group. </p>"""
    rules: NotRequired[
        "aws_sdk_securityhub.types.aws_waf_rule_group_rules_list.AwsWafRuleGroupRulesList"
    ]
    """<p>Provides information about the rules attached to the rule group. These rules identify the web requests that you want to allow, block, or count. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafRuleGroupDetails) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "rule_group_id" in value:
        out["RuleGroupId"] = value["rule_group_id"]
    if "rules" in value:
        import aws_sdk_securityhub.types.aws_waf_rule_group_rules_list

        out["Rules"] = (
            aws_sdk_securityhub.types.aws_waf_rule_group_rules_list.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafRuleGroupDetails:
    out: AwsWafRuleGroupDetails = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    if "Rules" in data:
        import aws_sdk_securityhub.types.aws_waf_rule_group_rules_list

        out["rules"] = (
            aws_sdk_securityhub.types.aws_waf_rule_group_rules_list.deserialize_json(
                data["Rules"]
            )
        )
    return out
