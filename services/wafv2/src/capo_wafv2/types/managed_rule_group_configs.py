"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.managed_rule_group_config

ManagedRuleGroupConfigs: TypeAlias = list[
    "capo_wafv2.types.managed_rule_group_config.ManagedRuleGroupConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupConfigs) -> list:
    import capo_wafv2.types.managed_rule_group_config

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.managed_rule_group_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedRuleGroupConfigs:
    import capo_wafv2.types.managed_rule_group_config

    out: ManagedRuleGroupConfigs = []
    for item in data:
        out.append(
            capo_wafv2.types.managed_rule_group_config.deserialize_aws_json_1_1(item)
        )
    return out
