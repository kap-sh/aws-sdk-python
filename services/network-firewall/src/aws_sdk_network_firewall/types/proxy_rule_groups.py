"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_group_metadata

ProxyRuleGroups: TypeAlias = list[
    "aws_sdk_network_firewall.types.proxy_rule_group_metadata.ProxyRuleGroupMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroups) -> list:
    import aws_sdk_network_firewall.types.proxy_rule_group_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_group_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleGroups:
    import aws_sdk_network_firewall.types.proxy_rule_group_metadata

    out: ProxyRuleGroups = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_group_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
