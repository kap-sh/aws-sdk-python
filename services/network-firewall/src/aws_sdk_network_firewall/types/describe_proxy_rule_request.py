"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeProxyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DescribeProxyRuleRequest(TypedDict, closed=True):
    proxy_rule_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProxyRuleRequest) -> dict:
    out: dict = {}
    out["ProxyRuleName"] = value["proxy_rule_name"]
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProxyRuleRequest:
    out: DescribeProxyRuleRequest = {}  # type: ignore[typeddict-item]
    if "ProxyRuleName" in data:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    else:
        raise DeserializationError("DescribeProxyRuleRequest.proxy_rule_name required")
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    return out
