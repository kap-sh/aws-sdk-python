"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.create_proxy_rule

CreateProxyRuleList: TypeAlias = list[
    "aws_sdk_network_firewall.types.create_proxy_rule.CreateProxyRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyRuleList) -> list:
    import aws_sdk_network_firewall.types.create_proxy_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.create_proxy_rule.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CreateProxyRuleList:
    import aws_sdk_network_firewall.types.create_proxy_rule

    out: CreateProxyRuleList = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.create_proxy_rule.deserialize_aws_json_1_0(
                item
            )
        )
    return out
