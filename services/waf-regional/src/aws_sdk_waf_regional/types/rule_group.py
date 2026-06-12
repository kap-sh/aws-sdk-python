"""Generated from Smithy shape ``com.amazonaws.wafregional#RuleGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.metric_name
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class RuleGroup(TypedDict):
    rule_group_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>RuleGroup</code>. You use <code>RuleGroupId</code> to get more information about a <code>RuleGroup</code> (see <a>GetRuleGroup</a>), update a <code>RuleGroup</code> (see <a>UpdateRuleGroup</a>), insert a <code>RuleGroup</code> into a <code>WebACL</code> or delete a one from a <code>WebACL</code> (see <a>UpdateWebACL</a>), or delete a <code>RuleGroup</code> from AWS WAF (see <a>DeleteRuleGroup</a>).</p> <p> <code>RuleGroupId</code> is returned by <a>CreateRuleGroup</a> and by <a>ListRuleGroups</a>.</p>"""
    name: NotRequired["aws_sdk_waf_regional.types.resource_name.ResourceName"]
    """<p>The friendly name or description for the <code>RuleGroup</code>. You can't change the name of a <code>RuleGroup</code> after you create it.</p>"""
    metric_name: NotRequired["aws_sdk_waf_regional.types.metric_name.MetricName"]
    """<p>A friendly name or description for the metrics for this <code>RuleGroup</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including \"All\" and \"Default_Action.\" You can't change the name of the metric after you create the <code>RuleGroup</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleGroup) -> dict:
    out: dict = {}
    out["RuleGroupId"] = value["rule_group_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleGroup:
    out: RuleGroup = {}  # type: ignore[typeddict-item]
    if "RuleGroupId" in data:
        out["rule_group_id"] = data["RuleGroupId"]
    else:
        raise DeserializationError("RuleGroup.rule_group_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    return out
