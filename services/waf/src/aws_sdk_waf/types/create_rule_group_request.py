"""Generated from Smithy shape ``com.amazonaws.waf#CreateRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.metric_name
    import aws_sdk_waf.types.resource_name
    import aws_sdk_waf.types.tag_list


class CreateRuleGroupRequest(TypedDict, closed=True):
    name: "aws_sdk_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>RuleGroup</a>. You can't change <code>Name</code> after you create a <code>RuleGroup</code>.</p>"""
    metric_name: "aws_sdk_waf.types.metric_name.MetricName"
    r"""<p>A friendly name or description for the metrics for this <code>RuleGroup</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including \"All\" and \"Default_Action.\" You can't change the name of the metric after you create the <code>RuleGroup</code>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    tags: NotRequired["aws_sdk_waf.types.tag_list.TagList"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["MetricName"] = value["metric_name"]
    out["ChangeToken"] = value["change_token"]
    if "tags" in value:
        import aws_sdk_waf.types.tag_list

        out["Tags"] = aws_sdk_waf.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleGroupRequest:
    out: CreateRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.name required")
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.metric_name required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("CreateRuleGroupRequest.change_token required")
    if "Tags" in data:
        import aws_sdk_waf.types.tag_list

        out["tags"] = aws_sdk_waf.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
