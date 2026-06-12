"""Generated from Smithy shape ``com.amazonaws.wafregional#SubscribedRuleGroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.metric_name
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class SubscribedRuleGroupSummary(TypedDict):
    rule_group_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>RuleGroup</code>.</p>"""
    name: "aws_sdk_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <code>RuleGroup</code>. You can't change the name of a <code>RuleGroup</code> after you create it.</p>"""
    metric_name: "aws_sdk_waf_regional.types.metric_name.MetricName"
    """<p>A friendly name or description for the metrics for this <code>RuleGroup</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including \"All\" and \"Default_Action.\" You can't change the name of the metric after you create the <code>RuleGroup</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedRuleGroupSummary) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    out["Name"] = value["name"]
    out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribedRuleGroupSummary:
    out: SubscribedRuleGroupSummary = {}  # type: ignore[typeddict-item]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.rule_group_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.name required")
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("SubscribedRuleGroupSummary.metric_name required")
    return out
