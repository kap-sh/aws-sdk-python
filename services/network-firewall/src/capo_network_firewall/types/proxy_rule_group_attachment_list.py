"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleGroupAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_group_attachment

ProxyRuleGroupAttachmentList: TypeAlias = list[
    "capo_network_firewall.types.proxy_rule_group_attachment.ProxyRuleGroupAttachment"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleGroupAttachmentList) -> list:
    import capo_network_firewall.types.proxy_rule_group_attachment

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.proxy_rule_group_attachment.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleGroupAttachmentList:
    import capo_network_firewall.types.proxy_rule_group_attachment

    out: ProxyRuleGroupAttachmentList = []
    for item in data:
        out.append(
            capo_network_firewall.types.proxy_rule_group_attachment.deserialize_aws_json_1_0(
                item
            )
        )
    return out
