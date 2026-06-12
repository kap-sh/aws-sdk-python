"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyRuleConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_rule_condition

ProxyRuleConditionList: TypeAlias = list[
    "aws_sdk_network_firewall.types.proxy_rule_condition.ProxyRuleCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyRuleConditionList) -> list:
    import aws_sdk_network_firewall.types.proxy_rule_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProxyRuleConditionList:
    import aws_sdk_network_firewall.types.proxy_rule_condition

    out: ProxyRuleConditionList = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.proxy_rule_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
