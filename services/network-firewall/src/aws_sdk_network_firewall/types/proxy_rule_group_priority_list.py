"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupPriorityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_group_priority

ProxyRuleGroupPriorityList: TypeAlias = list[
    "aws_sdk_network_firewall.types.proxy_rule_group_priority.ProxyRuleGroupPriority"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupPriorityList) -> list:
    import aws_sdk_network_firewall.types.proxy_rule_group_priority

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_group_priority.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleGroupPriorityList:
    import aws_sdk_network_firewall.types.proxy_rule_group_priority

    out: ProxyRuleGroupPriorityList = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_group_priority.deserialize_aws_json_1_0(
                item
            )
        )
    return out
