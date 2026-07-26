"""Generated from Smithy shape ``com.amazonaws.wafregional#SubscribedRuleGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.subscribed_rule_group_summary

SubscribedRuleGroupSummaries: TypeAlias = list[
    "capo_waf_regional.types.subscribed_rule_group_summary.SubscribedRuleGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedRuleGroupSummaries) -> list:
    import capo_waf_regional.types.subscribed_rule_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.subscribed_rule_group_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubscribedRuleGroupSummaries:
    import capo_waf_regional.types.subscribed_rule_group_summary

    out: SubscribedRuleGroupSummaries = []
    for item in data:
        out.append(
            capo_waf_regional.types.subscribed_rule_group_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
