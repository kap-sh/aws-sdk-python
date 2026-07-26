"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupPriorityResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_group_priority_result

ProxyRuleGroupPriorityResultList: TypeAlias = list[
    "capo_network_firewall.types.proxy_rule_group_priority_result.ProxyRuleGroupPriorityResult"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupPriorityResultList) -> list:
    import capo_network_firewall.types.proxy_rule_group_priority_result

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.proxy_rule_group_priority_result.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleGroupPriorityResultList:
    import capo_network_firewall.types.proxy_rule_group_priority_result

    out: ProxyRuleGroupPriorityResultList = []
    for item in data:
        out.append(
            capo_network_firewall.types.proxy_rule_group_priority_result.deserialize_aws_json_1_0(
                item
            )
        )
    return out
