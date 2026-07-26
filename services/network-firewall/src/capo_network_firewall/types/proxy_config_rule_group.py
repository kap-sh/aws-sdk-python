"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyConfigRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_config_rule_group_priority
    import capo_network_firewall.types.proxy_config_rule_group_type
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class ProxyConfigRuleGroup(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p>"""
    type: NotRequired[
        "capo_network_firewall.types.proxy_config_rule_group_type.ProxyConfigRuleGroupType"
    ]
    """<p>Proxy rule group type. </p>"""
    priority: NotRequired[
        "capo_network_firewall.types.proxy_config_rule_group_priority.ProxyConfigRuleGroupPriority"
    ]
    """<p>Priority of the proxy rule group in the proxy configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyConfigRuleGroup) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyConfigRuleGroup:
    out: ProxyConfigRuleGroup = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "ProxyRuleGroupArn" in data:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
