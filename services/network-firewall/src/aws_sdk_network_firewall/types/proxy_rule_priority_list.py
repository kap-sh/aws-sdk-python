"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRulePriorityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_priority

ProxyRulePriorityList: TypeAlias = list[
    "aws_sdk_network_firewall.types.proxy_rule_priority.ProxyRulePriority"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRulePriorityList) -> list:
    import aws_sdk_network_firewall.types.proxy_rule_priority

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_priority.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRulePriorityList:
    import aws_sdk_network_firewall.types.proxy_rule_priority

    out: ProxyRulePriorityList = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_priority.deserialize_aws_json_1_0(
                item
            )
        )
    return out
