"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule

ProxyRuleList: TypeAlias = list["capo_network_firewall.types.proxy_rule.ProxyRule"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleList) -> list:
    import capo_network_firewall.types.proxy_rule

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.proxy_rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleList:
    import capo_network_firewall.types.proxy_rule

    out: ProxyRuleList = []
    for item in data:
        out.append(
            capo_network_firewall.types.proxy_rule.deserialize_aws_json_1_0(item)
        )
    return out
