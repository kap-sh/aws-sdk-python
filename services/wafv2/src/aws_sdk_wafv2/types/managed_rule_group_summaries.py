"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.managed_rule_group_summary

ManagedRuleGroupSummaries: TypeAlias = list[
    "aws_sdk_wafv2.types.managed_rule_group_summary.ManagedRuleGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleGroupSummaries) -> list:
    import aws_sdk_wafv2.types.managed_rule_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wafv2.types.managed_rule_group_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedRuleGroupSummaries:
    import aws_sdk_wafv2.types.managed_rule_group_summary

    out: ManagedRuleGroupSummaries = []
    for item in data:
        out.append(
            aws_sdk_wafv2.types.managed_rule_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
