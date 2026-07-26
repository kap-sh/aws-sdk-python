"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupPriorityResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_group_priority_result_priority
    import capo_network_firewall.types.resource_name


class ProxyRuleGroupPriorityResult(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p>"""
    priority: NotRequired[
        "capo_network_firewall.types.proxy_rule_group_priority_result_priority.ProxyRuleGroupPriorityResultPriority"
    ]
    """<p>Priority of the proxy rule group in the proxy configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupPriorityResult) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ProxyRuleGroupPriorityResult:
    out: ProxyRuleGroupPriorityResult = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroupName" in data:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
