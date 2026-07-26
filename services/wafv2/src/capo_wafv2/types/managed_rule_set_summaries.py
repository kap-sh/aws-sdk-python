"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedRuleSetSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.managed_rule_set_summary

ManagedRuleSetSummaries: TypeAlias = list[
    "capo_wafv2.types.managed_rule_set_summary.ManagedRuleSetSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedRuleSetSummaries) -> list:
    import capo_wafv2.types.managed_rule_set_summary

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.managed_rule_set_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedRuleSetSummaries:
    import capo_wafv2.types.managed_rule_set_summary

    out: ManagedRuleSetSummaries = []
    for item in data:
        out.append(
            capo_wafv2.types.managed_rule_set_summary.deserialize_aws_json_1_1(item)
        )
    return out
