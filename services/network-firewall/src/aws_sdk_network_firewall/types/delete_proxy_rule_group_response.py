"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DeleteProxyRuleGroupResponse(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    proxy_rule_group_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRuleGroupResponse) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRuleGroupResponse:
    out: DeleteProxyRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    return out
