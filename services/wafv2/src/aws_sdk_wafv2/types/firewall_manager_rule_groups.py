"""Generated from Smithy shape ``com.amazonaws.wafv2#FirewallManagerRuleGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.firewall_manager_rule_group

FirewallManagerRuleGroups: TypeAlias = list[
    "aws_sdk_wafv2.types.firewall_manager_rule_group.FirewallManagerRuleGroup"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallManagerRuleGroups) -> list:
    import aws_sdk_wafv2.types.firewall_manager_rule_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wafv2.types.firewall_manager_rule_group.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FirewallManagerRuleGroups:
    import aws_sdk_wafv2.types.firewall_manager_rule_group

    out: FirewallManagerRuleGroups = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.firewall_manager_rule_group.deserialize_aws_json_1_1(
                item
            )
        )
    return out
